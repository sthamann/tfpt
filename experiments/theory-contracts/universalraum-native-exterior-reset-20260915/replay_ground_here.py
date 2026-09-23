"""Replay the already reviewed pinned ground proof in this research directory."""
from pathlib import Path
import importlib.util
import shutil

HERE=Path(__file__).resolve().parent
OLD=HERE.parent/'universalraum-native-ground-response-20260915'
target=HERE/'sources/replay_ground.py'
target.parent.mkdir(parents=True,exist_ok=True)
shutil.copy2(OLD/'replay_ground.py',target)
spec=importlib.util.spec_from_file_location('ground_source',target)
module=importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
module.HERE=HERE
module.SOURCE=OLD/'ground_replay'
module.OUT=HERE/'ground_replay'
try:
    module.main()
except BaseException as error:
    module.state['status']='FAIL'
    module.state['error']=repr(error)
    module.save()
    raise
