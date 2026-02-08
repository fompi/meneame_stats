{
  description = "Meneame stats analysis";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixpkgs-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = nixpkgs.legacyPackages.${system};
        rWithPackages = pkgs.rWrapper.override {
          packages = with pkgs.rPackages; [
            rmarkdown
            knitr
            dplyr
            car
            data_table
            ggplot2
            plotly
            lubridate
            tm
            wordcloud
            stringr
            RColorBrewer
          ];
        };
      in
      {
        devShells.default = pkgs.mkShell {
          packages = [
            rWithPackages
            pkgs.pandoc
          ];

          shellHook = ''
            echo "meneame_stats dev shell"
            echo "  R: $(R --version | head -1)"
            echo ""
            echo "Usage: Rscript -e \"rmarkdown::render('analisis.Rmd')\""
          '';
        };
      }
    );
}
