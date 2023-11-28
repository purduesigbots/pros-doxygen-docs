DOXYFILE = "Doxyfile-mcss"

FAVICON = "logo.png"
THEME_COLOR = "#e6b85c"
SHOW_UNDOCUMENTED = True

STYLESHEETS = [
    "./m.css/css/m-dark+documentation.compiled.css",
    "https://fonts.googleapis.com/css?family=Source+Sans+Pro:400,400i,600,600i%7CSource+Code+Pro:400,400i,600",
    "pros-custom.css",
    "pros-code.css",
]

LINKS_NAVBAR1 = [
    (None, "getting-started", []),
    (
        "None",
        "tutorials",
        [
            (None, "general-tutorials"),
            (None, "walkthrough-tutorials"),
            (None, "topical-tutorials"),
        ],
    ),
    ("API", "api", []),
    ("pros3", "https://pros.cs.purdue.edu/v5", []),
]

LINKS_NAVBAR2 = [
    (
        '<a href="#">Other</a>',
        [
            (None, "pages"),
            (None, "annotated"),
            (None, "modules"),
            (None, "namespaces"),
            (None, "files"),
        ],
    )
]
