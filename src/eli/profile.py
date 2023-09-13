"""

An Eli profile used to configure Eli behaviour for a specific use-case.
"""

from configurable import Configurable

class Profile(Configurable):
    """The base class for a Profile."""

    def __init__(
        self,
        name: str,
        debug: bool,
        cls_on_submit: bool,
        model: any,
        incl_docs: bool,
    ):
        self.name = name
        self.debug = debug
        self.cls_on_submit = cls_on_submit
        self.model = model
        self.incl_docs = incl_docs

    def new(name, debug, cls_on_submit, model, incl_docs):
        return Profile(
            name=name, debug=debug, cls_on_submit=cls_on_submit, model=model, incl_docs=incl_docs
        )


