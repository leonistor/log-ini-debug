from configparser import ConfigParser, ExtendedInterpolation

config = ConfigParser(interpolation=ExtendedInterpolation())

config.read("interpolation_config.ini")

for section in config.sections():
    print(f"--- {section} ---")
    for k, v in config.items(section=section):
        print(f"  {k}: {v}")
