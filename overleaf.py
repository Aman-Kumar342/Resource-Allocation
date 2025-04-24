import numpy as np
import matplotlib.pyplot as plt

# --- Dependencies ---
# 1. numpy: For numerical operations (arrays, linspace, etc.)
#    Install: pip install numpy
# 2. matplotlib: For creating plots and graphs
#    Install: pip install matplotlib

# Ensure a 'figures' directory exists
import os
if not os.path.exists("figures"):
    os.makedirs("figures")

# Nash Equilibrium VM Allocation
vm_allocation = [20, 20, 20]  # Example allocation
labels = ['P1', 'P2', 'P3']

plt.figure(figsize=(8, 6))
plt.bar(labels, vm_allocation, color='skyblue')
plt.xlabel('Provider')
plt.ylabel('Allocated VMs')
plt.title('Nash Equilibrium VM Allocation')
plt.grid(axis='y', linestyle='--')
plt.ylim(0, 22)  # Adjust y-axis limit for better visualization

# Add allocation numbers on top of the bars
for i, value in enumerate(vm_allocation):
    plt.text(i, value + 0.5, str(value), ha='center', va='bottom')

plt.tight_layout()
plt.savefig('figures/Nash Equilibrium VM Allocation.png')
plt.close()

# Provider Utilities at Nash Equilibrium
utilities = [280, 250, 220]  # Example utilities
plt.figure(figsize=(8, 6))
plt.bar(labels, utilities, color='lightgreen')
plt.xlabel('Provider')
plt.ylabel('Utility')
plt.title('Provider Utilities at Nash Equilibrium')
plt.grid(axis='y', linestyle='--')
plt.ylim(0, 300)  # Adjust y-axis limit

# Add utility numbers on top of the bars
for i, value in enumerate(utilities):
    plt.text(i, value + 5, str(value), ha='center', va='bottom')

plt.tight_layout()
plt.savefig('figures/Provider Utilities at Nash Equilibrium.png')
plt.close()

# Revenue and Cost Breakdown per Provider (Example Data)
revenue = [120, 150, 180]
usage_cost = [200, 180, 150]
fixed_cost = [50, 50, 50]

plt.figure(figsize=(8, 6))

x = np.arange(len(labels))  # the label locations
width = 0.5  # the width of the bars

plt.bar(x, revenue, width, label='Revenue', color='salmon')
plt.bar(x, usage_cost, width, bottom=revenue, label='Usage Cost', color='lightblue')
plt.bar(x, fixed_cost, width, bottom=[i + j for i, j in zip(revenue, usage_cost)],
        label='Fixed Cost', color='gray')

plt.ylabel('Value')
plt.xlabel('Provider')
plt.title('Revenue and Cost Breakdown per Provider')
plt.xticks(x, labels)
plt.legend()
plt.tight_layout()

plt.savefig('figures/Revenue and Cost Breakdown per Provider.png')
plt.close()

# Utility vs VMs Allocated (Assuming Others Allocate 10)
def utility(x):
    return 100 * np.log(x + 1)

x = np.linspace(0, 20, 100)
plt.figure(figsize=(8, 6))
plt.plot(x, utility(x), label='Provider 1')
plt.plot(x, utility(x - 2), label='Provider 2')
plt.plot(x, utility(x - 4), label='Provider 3')

plt.xlabel('VMs Allocated by Provider')
plt.ylabel('Utility')
plt.title('Utility vs VMs Allocated (Assuming Others Allocate 10)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig('figures/Utility vs VMs Allocated (Assuming Others Allocate 10).png')
plt.close()

# Price Function
def price_function(vms):
    if vms < 50:
        return 100 - (vms * 1.6)  # Adjust slope for visual appeal
    else:
        return 20  # Example flat price after 50 VMs

vms_range = np.arange(0, 61)
prices = [price_function(vms) for vms in vms_range]

plt.figure(figsize=(8, 6))
plt.plot(vms_range, prices, color='darkorange')
plt.xlabel('Total VMs Allocated')
plt.ylabel('Price per VM')
plt.title('Price Function')
plt.grid(True)
plt.ylim(15, 105)
plt.tight_layout()
plt.savefig('figures/Price Function.png')
plt.close()

print("Graphs generated and saved in the 'figures' directory.")