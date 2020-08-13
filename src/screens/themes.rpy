#
# themes.rpy
# Unscripted Core - Theme Engine
#
# Created by Marquis Kurt on 05/31/20.
# Copyright © 2020 Marquis Kurt. All rights reserved.
#

init offset = -100

init -100 python:
    import toml
    from enum import Enum
    from os import path

    class ThemeType(Enum):
        LIGHT = "light"
        DARK = "dark"

    class Theme(object):
        """A class representation of a theme."""

        def __init__(self, **kwargs):
            """Construct a theme object.

            Args:
                **kwargs: Arbitrary keyword arguments

            Kwargs:
                filepath (str): The path to a valid theme configuration.
                name (str): The name of the theme.
                path (str): The path to the file's theme resources.
            """

            self.name = "ring"
            self.path = ["core", "themes", "ring", "resources"]
            self.rpath = "/".join(self.path)
            self.type = ThemeType.DARK
            self._ui_colors = Enum("ThemeColor",
                        dict(
                            BACKGROUND="#2b2b2b",
                            INTERFACE="#f4f4f4",
                            INTERFACE_ACTIVE="#05C1FD",
                            INTERFACE_HIGHLIGHT="#5848F4",
                            INTERFACE_SECONDARY="#999999",
                            INTERFACE_BUTTON_IDLE="#f4f4f4"
                        ))
            self._syntax_colors = Enum("ThemeSyntaxColor",
                                    dict(
                                        SOURCE_TEXT="#A9B7C6",
                                        SYMBOLS="#A9B7C6",
                                        COMMENTS="#75715e",
                                        DOCSTRINGS="#75715e",
                                        STRINGS="#A5C25C",
                                        KEYWORDS="#CB772F",
                                        NUMBERS="#6897BB"
                                    ))

            for special in ["name", "path", "type"]:
                if special in kwargs:
                    self.__dict__[special] = kwargs[special]

            if "filepath" in kwargs:
                xpath = kwargs["filepath"]

                if renpy.loadable(xpath):
                    with renpy.file(xpath) as conf:
                        theme_conf = toml.load(conf)["theme"]

                        self.name = theme_conf["name"]
                        self.path = theme_conf["resources-dir"].split("/") + ["resources"]
                        self.rpath = "/".join(self.path)
                        self.type = ThemeType.LIGHT if theme_conf["type"] == "light"\
                            else ThemeType.DARK

                        colors = theme_conf["colors"].copy()
                        colors["syntax"] = None
                        new_colors = dict((k.upper(), v) for k, v in colors.iteritems())
                        syntax = dict(
                            (k.upper(), v) for k, v in theme_conf["colors"]["syntax"].iteritems()
                        )

                        self._ui_colors = Enum("ThemeColor", new_colors)
                        self._syntax_colors = Enum("ThemeSyntaxColor", syntax)

        def colors(self):
            """Get the theme's colors.

            Returns:
                ui_colors (ThemeColor): The theme's UI colors.
            """
            return self._ui_colors

        def syntaxes(self):
            """Get the theme's colors for syntax highlighting.

            Returns:
                syntax_colors (ThemeSyntaxColor): The theme's syntax colors.
            """
            return self._syntax_colors

        def checkboxes(self):
            """Get the paths for the theme's checkbox styles.

            Returns:
                checks (ThemeCheckbox): The theme's checkbox enumeration.
            """
            # bg = path.join(*self.path + ["checkboxes", self.name + "_[prefix_]background.png"])
            # fg = path.join(*self.path + ["checkboxes", self.name + "_[prefix_]foreground.png"])
            bg = self.rpath + "/checkboxes/" + self.name + "_[prefix_]background.png"
            fg = self.rpath + "/checkboxes/" + self.name + "_[prefix_]foreground.png"
            return Enum("ThemeCheckbox",
                        {
                            "BACKGROUND": bg,
                            "FOREGROUND": fg
                        })

        def radios(self):
            """Get the paths for the theme's radio styles.

            Returns:
                radios (ThemeRadio): The theme's radio enumeration.
            """
            # bg = path.join(*self.path + ["radios", self.name + "_[prefix_]background.png"])
            # fg = path.join(*self.path + ["radios", self.name + "_[prefix_]foreground.png"])
            bg = self.rpath + "/radios/" + self.name + "_[prefix_]background.png"
            fg = self.rpath + "/radios/" + self.name + "_[prefix_]foreground.png"
            # print(bg)
            return Enum("ThemeRadio",
                        {
                            "BACKGROUND": bg,
                            "FOREGROUND": fg
                        })

        def buttons(self):
            """Get the path for the theme's button styles.

            Returns:
                buttons (str): The path to the button images.
            """
            # return path.join(*self.path + ["buttons", self.name + "_[prefix_]background.png"])
            return self.rpath + "/buttons/" + self.name + "_[prefix_]background.png"

        def tabs(self):
            """Get the path for the theme's tab group styles.

            Returns:
                tabs (str): The path to the tab group images.
            """
            # return path.join(*self.path + ["tabs", self.name + "_[prefix_]background.png"])
            return self.rpath + "/tabs/" + self.name + "_[prefix_]background.png"

        def bars(self):
            """Get the paths for the theme's bar styles.

            Returns:
                bars (ThemeBars): The theme's bars enumeration.
            """
            # top = path.join(*self.path + ["bars", self.name + "_top.png"])
            # left = path.join(*self.path + ["bars", self.name + "_left.png"])
            # right = path.join(*self.path + ["bars", self.name + "_right.png"])
            # bottom = path.join(*self.path + ["bars", self.name + "_bottom.png"])
            top =  self.rpath + "/bars/" + self.name + "_top.png"
            right =  self.rpath + "/bars/" + self.name + "_right.png"
            left =  self.rpath + "/bars/" + self.name + "_left.png"
            bottom =  self.rpath + "/bars/" + self.name + "_bottom.png"

            return Enum("ThemeBars",
                        {
                            "TOP": top,
                            "LEFT": left,
                            "RIGHT": right,
                            "BOTTOM": bottom
                        })

        def scrollbars(self):
            """Get the paths for the theme's scrollbar styles.

            Returns:
                scrollbars (ThemeScrollbars): The theme's scrollbars enumeration.
            """
            # horiz = path.join(*self.path + ["scrollers",
            #                                     self.name + "_horizontal_[prefix_]bar.png"])
            # verti = path.join(*self.path + ["scrollers", self.name + "_vertical_[prefix_]bar.png"])
            # h_thumb = path.join(*self.path + ["scrollers",
            #                                     self.name + "_horizontal_[prefix_]thumb.png"])
            # v_thumb = path.join(*self.path + ["scrollers",
            #                                     self.name + "_vertical_[prefix_]thumb.png"])
            horiz = self.rpath + "/scrollers/" + self.name + "_horizontal_[prefix_]bar.png"
            verti = self.rpath + "/scrollers/" + self.name + "_vertical_[prefix_]bar.png"
            h_thumb = self.rpath + "/scrollers/" + self.name + "_horizontal_[prefix_]thumb.png"
            v_thumb = self.rpath + "/scrollers/" + self.name + "_vertical_[prefix_]thumb.png"
            return Enum("ThemeScrollbars",
                        {
                            "HORIZONTAL": horiz,
                            "HORIZONTAL_THUMB": h_thumb,
                            "VERTICAL": verti,
                            "VERTICAL_THUMB": v_thumb
                        })

        def sliders(self):
            """Get the paths for the theme's slider styles.

            Returns:
                sliders (ThemeSliders): The theme's scrollbars enumeration.
            """
            # horiz = path.join(*self.path + ["sliders", self.name + "_horizontal_[prefix_]bar.png"])
            # verti = path.join(*self.path + ["sliders", self.name + "_vertical_[prefix_]bar.png"])
            # h_thumb = path.join(*self.path + ["sliders",
            #                                     self.name + "_horizontal_[prefix_]thumb.png"])
            # v_thumb = path.join(*self.path + ["sliders",
            #                                     self.name + "_vertical_[prefix_]thumb.png"])
            horiz = self.rpath + "/sliders/" + self.name + "_horizontal_[prefix_]bar.png"
            verti = self.rpath + "/sliders/" + self.name + "_vertical_[prefix_]bar.png"
            h_thumb = self.rpath + "/sliders/" + self.name + "_horizontal_[prefix_]thumb.png"
            v_thumb = self.rpath + "/sliders/" + self.name + "_vertical_[prefix_]thumb.png"
            return Enum("ThemeSliders",
                        {
                            "HORIZONTAL": horiz,
                            "HORIZONTAL_THUMB": h_thumb,
                            "VERTICAL": verti,
                            "VERTICAL_THUMB": v_thumb
                        })

        def frames(self):
            """Get the paths for the theme's frame styles.

            Returns:
                frames (ThemeFrame): The theme's frame enumeration.
            """
            # basic = path.join(*self.path + ["frames", self.name + "_basic.png"])
            # toast = path.join(*self.path + ["frames", self.name + "_toast.png"])
            # narrative = path.join(*self.path + ["frames", self.name + "_narrative.png"])
            # textbox = path.join(*self.path + ["frames", self.name + "_textbox.png"])
            # name = path.join(*self.path + ["frames", self.name + "_namebox.png"])
            basic = self.rpath + "/frames/" + self.name + "_basic.png"
            toast = self.rpath + "/frames/" + self.name + "_toast.png"
            narrative = self.rpath + "/frames/" + self.name + "_narrative.png"
            textbox = self.rpath + "/frames/" + self.name + "_textbox.png"
            name = self.rpath + "/frames/" + self.name + "_namebox.png"

            return Enum("ThemeFrame",
                        {
                            "BASIC": basic,
                            "TOAST": toast,
                            "NARRATIVE": narrative,
                            "TEXTBOX": textbox,
                            "NAME": name
                        })

        def overlays(self):
            """Get the paths for the theme's overlay styles.

            Returns:
                overlays (overlay): The theme's overlay enumeration.
            """
            # confirm = path.join(*self.path + ["overlays", self.name + "_confirm.png"])
            # main = path.join(*self.path + ["overlays", self.name + "_main_menu.png"])
            # game = path.join(*self.path + ["overlays", self.name + "_game_menu.png"])
            confirm = self.rpath + "/overlays/" + self.name + "_confirm.png"
            main = self.rpath + "/overlays/" + self.name + "_main_menu.png"
            game = self.rpath + "/overlays/" + self.name + "_game_menu.png"

            return Enum("ThemeOverlay",
                        {
                            "CONFIRM": confirm,
                            "MAIN": main,
                            "GAME": game
                        })
