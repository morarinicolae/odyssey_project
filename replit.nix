{pkgs}: {
  deps = [
    pkgs.rustc
    pkgs.libiconv
    pkgs.cargo
    pkgs.glibcLocales
    pkgs.libxcrypt
    pkgs.libuv
    pkgs.cacert
  ];
}
