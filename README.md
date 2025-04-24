# Game-Theoretic Resource Allocation in Cloud Computing

This repository contains the LaTeX source code, simulation scripts, and generated figures for a research paper exploring game-theoretic approaches to resource allocation in cloud computing environments. The project aims to address the challenges of efficiently distributing limited computational resources among competing users while maintaining fairness and system stability.

## Overview

Cloud computing resource allocation is a critical problem impacting system performance, user satisfaction, and provider revenue. Traditional allocation methods often prioritize either utilization or fairness, leading to suboptimal outcomes. This research proposes a game-theoretic framework that models resource allocation as a strategic interaction between users and providers.

The project employs two complementary approaches:

1.  **Non-Cooperative Game Model:** This model converges to a Nash Equilibrium, ensuring no user benefits from unilateral strategy changes.
2.  **Bargaining Game Model:** This model optimizes collective utility through cooperative negotiations.

Mathematical analysis integrates an M/M/n/n+l queuing model to quantify system behavior under dynamic workloads. Python simulations are used to validate the proposed models and analyze their performance.

## Project Structure

The repository is organized as follows:

- `figures/`: Contains the generated figures illustrating simulation results:

  - `Nash Equilibrium VM Allocation.png`: Shows the VM allocation for each provider under the Nash Equilibrium. Notice the relatively even distribution suggesting a balanced competitive environment.
  - `Price Function.png`: Depicts the price function, demonstrating a decreasing trend for VM allocations under 50 and a stable price thereafter. The price depends on the number of allocated VMs, not on which provider is allocating them.
  - `Provider Utilities at Nash Equilibrium.png`: Illustrates the utility achieved by each provider once the Nash Equilibrium is established. Provider utilities are not perfectly equal, which reflects differences in underlying costs or other factors.
  - `Revenue and Cost Breakdown per Provider.png`: Displays the revenue and cost breakdown (usage cost and fixed cost) for each provider. Analyze this graph to understand the key factors impacting the profit of the business.
  - `Utility vs VMs Allocated (Assuming Others Allocate 10).png`: Showcases how utility changes as the number of VMs allocated to one provider shifts, assuming other providers allocate 10 VMs each. The graph visualizes diminishing returns, as higher allocation yields a higher benefit.

- `venv/`: (Potentially) Contains a virtual environment for managing Python dependencies (if one was created).
- `.gitignore`: Specifies intentionally untracked files that Git should ignore.
- `main.tex`: The main LaTeX source file for the research paper.
- `overleaf.py`: A Python script used to generate data and images for the simulation.

## Key Findings

The research demonstrates the following key findings (visualized in the figures):

- **Balanced VM Allocation:** The Nash Equilibrium allocation results in a relatively balanced VM allocation among providers, promoting a competitive market (see `Nash Equilibrium VM Allocation.png`).
- **Variable Provider Utility:** Even under Nash equilibrium, provider utilities differ (see `Provider Utilities at Nash Equilibrium.png`), reflecting differing cost structures.
- **Revenue and Cost Insights:** Understanding the key factor impacting the business, with the given graph (see `Revenue and Cost Breakdown per Provider.png`)
- **Diminishing Returns for the higher utility graph:** For the number of VMs allocation to one provider shifts assuming others provide more (see `Utility vs VMs Allocated (Assuming Others Allocate 10).png`).
- **Pricing Model:** The price function decreases for the number of allocated VMs under 50 and stays constant. This is useful (see `Price Function.png`).

## Dependencies

To compile the LaTeX document and run the simulations, you will need the following dependencies:

- **LaTeX Distribution:** A TeX distribution such as TeX Live, MacTeX, or MiKTeX is required to compile the `main.tex` file.
- **Python 3:** Python 3 is required to run the simulation script (`overleaf.py`).
- **Python Libraries:** The following Python libraries are required:
  - `numpy`: For numerical operations. Install with: `pip install numpy`
  - `matplotlib`: For creating plots and graphs. Install with: `pip install matplotlib`

## Instructions

1.  **Clone the Repository:**

    ```bash
    git clone [repository URL]
    cd [repository directory]
    ```

2.  **Set up a Python Environment (Recommended):**

    - Create a virtual environment (optional, but recommended to isolate dependencies):

      ```bash
      python3 -m venv venv
      source venv/bin/activate  # On Linux/macOS
      venv\Scripts\activate  # On Windows
      ```

3.  **Install Python Dependencies:**

    ```bash
    pip install numpy matplotlib
    ```

4.  **Generate the Figures:**

    - Run the `overleaf.py` script:

      ```bash
      python overleaf.py
      ```

      This will generate the image files in the `figures/` directory.

5.  **Compile the LaTeX Document:**

    - Compile the `main.tex` file using your preferred LaTeX compiler (e.g., `pdflatex`, `xelatex`):

      ```bash
      pdflatex main.tex
      ```

      You may need to run this command multiple times to resolve all cross-references.

6.  **View the PDF:**

    - Open the generated PDF file (`main.pdf`) to view the compiled research paper.

## License

[Specify the license under which the project is released (e.g., MIT License, Apache 2.0 License). Add a LICENSE file in the root directory with the full license text.]
