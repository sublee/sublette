exports.decorateConfig = config => {
  return Object.assign({}, config, {
    foregroundColor: "#ccced0",
    backgroundColor: "#202535",

    colors: {
      black:   "#253045",
      red:     "#e57",
      green:   "#5e7",
      yellow:  "#fd8",
      blue:    "#58f",
      magenta: "#f7c",
      cyan:    "#4ee",
      white:   "#f5f5da",

      lightBlack:   "#405570",
      lightRed:     "#e65",
      lightGreen:   "#9e7",
      lightYellow:  "#ff7",
      lightBlue:    "#7bf",
      lightMagenta: "#a8f",
      lightCyan:    "#5fb",
      lightWhite:   "#ffe",
    },

    cursorColor:       "#ccced0",
    cursorAccentColor: "#202535",
    selectionColor:    "rgba(85,136,255, 0.3)",

    borderColor: "#253045",
    css: `
      ${config.css || ''}

      .tabs_list .tab_tab {
        background: #253045;
        color: #405570;
      }

      .tabs_list .tab_active {
        background: transparent;
        color: inherit;
      }

      .tabs_list .tab_hasActivity {
        color: #e57;
      }
    `
  })
}
