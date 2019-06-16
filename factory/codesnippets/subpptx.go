package subpptx

import (
	"github.com/beevik/etree"
)

// Finds and removes elements
func removeElements(elem *etree.Element, path string) {
	for _, e := range elem.FindElements(path) {
		e.Parent().RemoveChild(e)
	}
}
