exports.decorateConfig = config => {
  return Object.assign({}, config, {
    foregroundColor: "%(Foreground)s",
    backgroundColor: "%(Background)s",

    colors: {
      black:   "%(Black)s",
      red:     "%(Red)s",
      green:   "%(Green)s",
      yellow:  "%(Yellow)s",
      blue:    "%(Blue)s",
      magenta: "%(Magenta)s",
      cyan:    "%(Cyan)s",
      white:   "%(White)s",

      lightBlack:   "%(Bright Black)s",
      lightRed:     "%(Bright Red)s",
      lightGreen:   "%(Bright Green)s",
      lightYellow:  "%(Bright Yellow)s",
      lightBlue:    "%(Bright Blue)s",
      lightMagenta: "%(Bright Magenta)s",
      lightCyan:    "%(Bright Cyan)s",
      lightWhite:   "%(Bright White)s",
    },

    cursorColor:       "%(Foreground)s",
    cursorAccentColor: "%(Background)s",
    selectionColor:    "rgba(%(rgb[Bright Blue])s, 0.3)",

    borderColor: "%(Black)s",
    css: `
      ${config.css || ''}

      .tabs_title, .header_windowHeader {
        color: %(Foreground)s;
      }

      .tabs_list .tab_tab {
        background: %(Black)s;
        color: %(Bright Black)s;
      }

      .tabs_list .tab_active {
        background: %(Background)s;
        color: %(Foreground)s;
      }

      .tabs_list .tab_hasActivity {
        color: %(Red)s;
      }
    `
  })
}
