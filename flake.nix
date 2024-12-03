{
  description = "A Nix-flake-based Python development environment";

  inputs.nixpkgs.url = "github:NixOS/nixpkgs/nixos-24.05";

  outputs = { self, nixpkgs }:
    let
      supportedSystems = [ "x86_64-linux" "aarch64-linux" "x86_64-darwin" "aarch64-darwin" ];
      forEachSupportedSystem = f: nixpkgs.lib.genAttrs supportedSystems (system: f {
        pkgs = import nixpkgs { inherit system; };
      });
    in
    {
      devShells = forEachSupportedSystem ({ pkgs }: {
        default = 
        let
          pythonPackages = pkgs.python311Packages;
        in
        pkgs.mkShell {
          venvDir = ".venv";
          packages = with pkgs; [ 
          ] ++
          (with pythonPackages; [
            python
            python-lsp-server
            pip
            venvShellHook
            numpy
          ]);
        };
      });
    };
}
