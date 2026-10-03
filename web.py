"""Simple browser dashboard for AI-LAB. It does not execute generated projects."""
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import html, webbrowser
from pathlib import Path
from tempfile import NamedTemporaryFile
from urllib.parse import parse_qs
from ai_lab.io import load_requirement
from ai_lab.validator import validate
from ai_lab.planner import build_plan

HOST,PORT="127.0.0.1",8766
PAGE="""<!doctype html><html><head><meta charset="utf-8"><title>AI-LAB</title><style>
body{font-family:Arial;max-width:950px;margin:40px auto;padding:0 20px;background:#f5f7fb}textarea,button{font:inherit}textarea{width:100%;height:220px;padding:12px}button{padding:11px;margin-top:10px;cursor:pointer}.card{background:white;padding:24px;border-radius:14px;box-shadow:0 2px 12px #0001}pre{background:#111;color:#eee;padding:18px;overflow:auto;border-radius:8px}.error{color:#b00020}</style></head>
<body><div class="card"><h1>AI-LAB</h1><p>Describe the AI project you want to build. AI-LAB will turn it into a structured project requirement and plan.</p>
<form method="post"><textarea name="idea" placeholder="Example: Build a local assistant that answers questions and uses an open-source model."></textarea><br><button>MAKE PLAN</button></form>RESULT</div></body></html>"""
def make_yaml(idea):
    safe=idea.replace('"','').strip()
    return f'''name: MyProject
purpose: "{safe}"
inputs:
  - user_text
outputs:
  - project_output
capabilities:
  - user-defined
constraints:
  - run locally when practical
  - do not hard-code secrets
preferred_language: python
execution_mode: review-first
'''
class Handler(BaseHTTPRequestHandler):
    def do_GET(self): self.send("")
    def do_POST(self):
        n=int(self.headers.get("Content-Length","0")); data=parse_qs(self.rfile.read(n).decode()); idea=data.get("idea",[""])[0].strip()
        if not idea: return self.send("")
        try:
            with NamedTemporaryFile("w",suffix=".yaml",delete=False,encoding="utf-8") as f: f.write(make_yaml(idea)); path=f.name
            req=load_requirement(path); diagnostics=validate(req)
            errors=[d.format() for d in diagnostics]
            plan=build_plan(req).to_dict() if not any(d.severity=="ERROR" for d in diagnostics) else {}
            result=f"<h2>Requirement</h2><pre>{html.escape(make_yaml(idea))}</pre><h2>Plan</h2><pre>{html.escape(str(plan))}</pre>"
            if errors: result+="<h2>Validation</h2><pre>"+html.escape("\n".join(errors))+"</pre>"
            self.send(result)
        except Exception as e: self.send("<div class='error'><b>Error:</b> "+html.escape(str(e))+"</div>")
    def send(self,result):
        raw=PAGE.replace("RESULT",result).encode(); self.send_response(200); self.send_header("Content-Type","text/html; charset=utf-8"); self.send_header("Content-Length",str(len(raw))); self.end_headers(); self.wfile.write(raw)
if __name__=="__main__":
    server=ThreadingHTTPServer((HOST,PORT),Handler); url=f"http://{HOST}:{PORT}"; print(url); webbrowser.open(url)
    try: server.serve_forever()
    except KeyboardInterrupt: pass
    finally: server.server_close()
