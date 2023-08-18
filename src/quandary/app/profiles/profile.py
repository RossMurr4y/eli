
class Profile():
    """A profile that defines a unique set of quandary configuration options."""

    OPTIONS = [
        ("Default", 0),
        ("Debugger", 1),
    ]

    def __init__(self, name: str, debug: bool):

        # the name of the profile
        self.name = name

        # debug mode enabled in this profile?
        self.debug = debug

    def get_profile_options(profiles):
        """generates a list of options (as a tuple) from a list of profiles"""
        opts = []
        i = 0
        for profile in profiles:
            opts.append((profile.name, i))
            i += 1
        return opts