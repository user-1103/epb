{
    description = "Imutable STIG Hardener For Ubuntu";

    inputs = {
        flake-utils.url = "github:numtide/flake-utils";
        nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
        poetry2nix = {
            url = "github:nix-community/poetry2nix";
            inputs.nixpkgs.follows = "nixpkgs";
        };
    };

    outputs = { self, nixpkgs, flake-utils, poetry2nix }:
        flake-utils.lib.eachDefaultSystem (
        system:
            let
                pkgs = nixpkgs.legacyPackages.${system};
                pkgs_overriden = pkgs.appendOverlays [poetry2nix.overlays.default];
                p2n = pkgs_overriden.poetry2nix;
            in
                {
                    o = poetry2nix;
                    k = p2n.mkPoetryApplication;
                    packages = {
                        epb = p2n.mkPoetryApplication { 
                            projectDir = self;
                            overrides = p2n.defaultPoetryOverrides.extend
                                (self: super: {
                                    scantree = super.scantree.overridePythonAttrs(
                                        old: {
                                            buildInputs = (old.buildInputs or [ ]) ++ [ super.setuptools ];
                                        }
                                    );
                                    dirhash = super.dirhash.overridePythonAttrs(
                                        old: {
                                            buildInputs = (old.buildInputs or [ ]) ++ [ super.setuptools ];
                                        }
                                    );
                                });
                        };
                        default = self.packages.${system}.epb;
                    };
                    devShells.default = pkgs.mkShell {
                        inputsFrom = [ self.packages.${system}.epb ];
                        packages = [ pkgs.poetry ];
                    };
                }
        );
}
