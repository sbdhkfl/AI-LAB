from ai_lab.io import load_requirement

def test_yaml(tmp_path):
    p=tmp_path/"req.yaml"; p.write_text("name: Demo\npurpose: A demo assistant for testing.\noutputs: [text]\n",encoding="utf-8")
    r=load_requirement(p); assert r.name=="Demo"; assert r.outputs==["text"]
