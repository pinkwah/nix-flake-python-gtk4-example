{
  inputs.nixpkgs.url = "nixpkgs";

  outputs = { nixpkgs, ... }:
    let

      system = "x86_64-linux";
      pkgs = import nixpkgs { inherit system; };

    in {
      devShells.${system}.default = pkgs.mkShell {
        packages = with pkgs; [
          gtk4
          gobject-introspection
          libadwaita
          (python3.withPackages (ps: with ps; [ pygobject3 pygobject-stubs pyright mypy ]))
        ];

        shellHook = ''
        '';
      };
    };
}
