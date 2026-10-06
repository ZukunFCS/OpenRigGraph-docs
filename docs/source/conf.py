from __future__ import annotations

project = "OpenRigGraph"
author = "OpenRigGraph contributors"
copyright = "2026, OpenRigGraph contributors"

extensions: list[str] = []
templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
html_title = "OpenRigGraph Documentation"

release = "2026.10.06"
version = release
nitpicky = True
nitpick_ignore = [("c:identifier", "size_t"), ("c:identifier", "uint32_t")]
html_show_sourcelink = True
html_theme_options = {"navigation_depth": 3}
html_context = {
    "display_github": True,
    "github_user": "ZukunFCS",
    "github_repo": "OpenRigGraph-docs",
    "github_version": "main",
    "conf_py_path": "/docs/source/",
}
