exports.decorateConfig = config => {
  return Object.assign({}, config, {
    foregroundColor: "#ccced0",
    backgroundColor: "#202535",

    colors: {
      black:   "#253045",
      red:     "#ee5577",
      green:   "#55ee77",
      yellow:  "#ffdd88",
      blue:    "#5588ff",
      magenta: "#ff77cc",
      cyan:    "#44eeee",
      white:   "#f5f5da",

      lightBlack:   "#405570",
      lightRed:     "#ee6655",
      lightGreen:   "#99ee77",
      lightYellow:  "#ffff77",
      lightBlue:    "#77bbff",
      lightMagenta: "#aa88ff",
      lightCyan:    "#55ffbb",
      lightWhite:   "#ffffee",
    },

    cursorColor:       "#ccced0",
    cursorAccentColor: "#202535",
    selectionColor:    "rgba(85,136,255, 0.3)",

    borderColor: "#253045",
    css: `
      ${config.css || ''}

      .tabs_title, .header_windowHeader {
        color: #ccced0;
      }

      .tabs_list .tab_tab {
        background: #253045;
        color: #405570;
      }

      .tabs_list .tab_active {
        background: transparent;
        color: #ccced0;
      }

      .tabs_list .tab_hasActivity {
        color: #ee5577;
      }
    `
  })
}
