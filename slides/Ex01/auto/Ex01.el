;; -*- lexical-binding: t; -*-

(TeX-add-style-hook
 "Ex01"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-class-options
                     '(("beamer" "10pt")))
   (TeX-add-to-alist 'LaTeX-provided-package-options
                     '(("ctex" "") ("fontspec" "") ("amsfonts" "") ("amsthm" "") ("bm" "") ("siunitx" "") ("xcolor" "") ("graphicx" "") ("longtable" "") ("wrapfig" "") ("rotating" "") ("ulem" "normalem") ("amsmath" "") ("amssymb" "") ("capt-of" "") ("hyperref" "") ("etoolbox" "") ("pgfopts" "") ("booktabs" "") ("ccicons" "scale=2")))
   (add-to-list 'LaTeX-verbatim-environments-local "semiverbatim")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "path")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "url")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "nolinkurl")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "hyperbaseurl")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "hyperimage")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "href")
   (add-to-list 'LaTeX-verbatim-macros-with-delims-local "path")
   (TeX-run-style-hooks
    "latex2e"
    "beamer"
    "beamer10"
    "ctex"
    "fontspec"
    "amsfonts"
    "amsthm"
    "bm"
    "siunitx"
    "xcolor"
    "graphicx"
    "longtable"
    "wrapfig"
    "rotating"
    "ulem"
    "amsmath"
    "amssymb"
    "capt-of"
    "hyperref"
    "etoolbox"
    "pgfopts"
    "booktabs"
    "ccicons")
   (LaTeX-add-labels
    "sec:orge4e0772"
    "sec:org8e580e9"
    "eq:1"
    "eq:2"
    "sec:orgc25006c"
    "eq:3"
    "eq:4"
    "sec:orgf6ca842")
   (LaTeX-add-bibliographies
    "reference.bib"))
 :latex)

