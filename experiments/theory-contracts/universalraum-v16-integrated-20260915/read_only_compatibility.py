"""Run the inspected compatibility computation without its output-writing tail."""
from pathlib import Path
import ast,json,sys
p=Path(sys.argv[1]); tree=ast.parse(p.read_text())
tail=tree.body[-2:]
if not (len(tail)==2 and isinstance(tail[0],ast.Expr)
        and isinstance(tail[0].value,ast.Call)
        and isinstance(tail[0].value.func,ast.Attribute)
        and tail[0].value.func.attr=='write_text'
        and isinstance(tail[1],ast.Expr)
        and isinstance(tail[1].value,ast.Call)
        and isinstance(tail[1].value.func,ast.Name)
        and tail[1].value.func.id=='print'):
    raise RuntimeError('Inspected output boundary changed')
env={'__name__':'readonly_compatibility','__file__':str(p)}
exec(compile(ast.Module(body=tree.body[:-2],type_ignores=[]),str(p),'exec'),env)
print(json.dumps(env['report'],indent=2))
