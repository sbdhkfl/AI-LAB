"""AI-LAB command line interface."""
import argparse,json,sys
from .io import load_requirement
from .validator import validate
from .planner import build_plan
from .registry import ModelRegistry
from .generator import generate_manifest

def main(argv=None):
    p=argparse.ArgumentParser(prog="ai-lab"); s=p.add_subparsers(dest="command",required=True)
    for n in ("plan","validate"):
        x=s.add_parser(n); x.add_argument("requirement")
    x=s.add_parser("generate"); x.add_argument("requirement"); x.add_argument("destination")
    s.add_parser("models"); a=p.parse_args(argv)
    try:
        if a.command=="models":
            for m in ModelRegistry().list(): print(f"{m.name} | {m.family} | {m.license}")
            return 0
        req=load_requirement(a.requirement); ds=validate(req)
        if a.command=="validate":
            for d in ds: print(d.format())
            if not ds: print("VALID: requirement passed AI-LAB validation.")
            return 1 if any(d.severity=="ERROR" for d in ds) else 0
        if any(d.severity=="ERROR" for d in ds):
            for d in ds: print(d.format(),file=sys.stderr)
            return 1
        if a.command=="plan": print(json.dumps(build_plan(req).to_dict(),indent=2))
        else: print(generate_manifest(req,a.destination))
        return 0
    except (OSError,ValueError,json.JSONDecodeError) as exc:
        print(f"[ERROR] AI001: {exc}",file=sys.stderr); return 2
