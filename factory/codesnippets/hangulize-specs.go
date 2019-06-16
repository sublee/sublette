package hangulize

import (
	"sort"
	"strings"

	"github.com/gobuffalo/packr"
)

// The box for HGL files.
var hgls = packr.NewBox("./hgls")

const ext = `.hgl`

// ListLangs returns the language name list of bundled specs.
// The bundled spec can be loaded by LoadSpec.
func ListLangs() []string {
	var langs []string

	for _, filename := range hgls.List() {
		if strings.HasSuffix(filename, ext) {
			langs = append(langs, strings.TrimSuffix(filename, ext))
		}
	}

	sort.Strings(langs)
	return langs
}
