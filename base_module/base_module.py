

from typing import Optional

from flask import Flask


cnt = [1]

class BaseModule:
    def __init__(self, app: Optional[Flask] = None) -> None:
        self._app = app
        print(f"module (name: {__name__}, initialized {'with' if app else 'without'} app context.")

    def init_app(self, app:Flask) -> None:
        self._app = app

    def app(self) -> Flask:
        if not self._app:
            raise Exception("App not initialized, please call init_app first.")
        return self._app

    def config(self):
        return self.app().config

    def names(self):
        return self.config()["names"]


print(f"module {__name__} run.")