import os
import os.path


def is_desktop(platform):
    return platform in ["windows", "macos", "linuxbsd", "uwp", "haiku"]


def is_unix_like(platform):
    return platform in ["macos", "linuxbsd", "android", "haiku", "ios"]


def module_supports_tools_on(platform):
    return is_desktop(platform)


def configure(env, env_mono):
    # is_android = env["platform"] == "android"
    # is_web = env["platform"] == "web"
    # is_ios = env["platform"] == "ios"
    # is_ios_sim = is_ios and env["arch"] in ["x86_32", "x86_64"]

    tools_enabled = env["tools"]

    if tools_enabled and not module_supports_tools_on(env["platform"]):
        raise RuntimeError("This module does not currently support building for this platform with tools enabled")

    if env["tools"]:
        env_mono.Append(CPPDEFINES=["GD_MONO_HOT_RELOAD"])
