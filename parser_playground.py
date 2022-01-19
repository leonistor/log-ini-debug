from configparser import ConfigParser

config = ConfigParser()
config.read("config.ini")

print(f"Sections: {config.sections()}")

option_admin = config.getboolean("admin", "moderator_page")

print(f"[admin]moderator_page: {option_admin}")

config.add_section("mysection")
config.set("mysection", "avalue", "3.14")
config.remove_section("moderator")

print(f"Options in admin section: {config.items('admin')}")

with open("config_modified.ini", "w") as f:
    config.write(f)
