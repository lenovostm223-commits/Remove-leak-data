{ pkgs }: {
  deps = [
    pkgs.python310
    pkgs.tor
    pkgs.torsocks
    pkgs.stem
    pkgs.openssl
  ];
}
