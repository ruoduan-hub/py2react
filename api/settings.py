from dotenv import load_dotenv
load_dotenv()

# 或者加一个配置，会默认覆盖已有环境变量的配置，推荐
load_dotenv(verbose=True)

# 或者，指定配置文件地址
from pathlib import Path  # python3 only
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)
