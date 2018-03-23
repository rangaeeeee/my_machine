(require 'package)
(setq package-enable-at-startup nil)
(add-to-list 'package-archives '("melpa" . "https://melpa.org/packages/"))
(add-to-list 'package-archives '("org" . "http://orgmode.org/elpa/") t)
(package-initialize)

;; bootstrap use package
(unless (package-installed-p 'use-package)
  (package-refresh-contents)
  (package-install 'use-package))

;; load the spacemacs-dark theme
(load-theme 'spacemacs-dark t)

(setenv "PYTHONIOENCODING" "utf-8")
(setenv "LANG" "en_US.UTF-8")
(require 'python)
(setq python-shell-interpreter "ipython")
(setq python-shell-interpreter-args "--pylab")
(setenv "IPY_TEST_SIMPLE_PROMPT" "1")
(org-babel-load-file (expand-file-name "~/.emacs.d/myinit.org"))

