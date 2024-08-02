# Chapter 12: Lab Example 2

## Overview

In this lab example, we will combine some concepts you have learned from the textbook: neurostimulation (Chapter 7), BCIs (Chapter 6), and disorders (Chapter 12). As you have learned, neurostimulation can modulate neural activity to alleviate symptoms of conditions such as Parkinson's disease, chronic pain, epilepsy, and depression. For instance, deep brain stimulation (DBS) is a widely used form of neurostimulation that targets brain regions to reduce tremors and improve motor function in Parkinson's patients. Similarly, spinal cord stimulation (SCS) is employed to manage chronic pain by altering pain signal transmission in the spinal cord.

In this lab example, we are going to be using the coil design from the Chapter 6: Lab Example and use it to simulate neurostimulation between simulated Parkinson’s Disease and Depression. We will then perform some statistical analysis (like the one in Chapter 5: Lab Example 2) to see how neurostimulation impacts these disorders differently.

## Requirements

- MATLAB (tested with R2021a and later)

## Steps

The first thing you need to do is go to the GitHub repository for this book. You can find it using this link:
[GitHub Repository](https://github.com/bddupre92/Neurobook_BME_UND)

After you have opened the GitHub, you need to navigate to Chapter 12 Lab Example 2. In this lab example, you will find three codes:
- Rtmscoildepression.m
- Rtmscoilforjustparkinsons.m
- Ttestrtmscoil.m

You will want to copy and paste each code into its own separate script.

We will first run the RTMS Coil for Parkinson’s and then the RTMS Coil for Depression. The scripts follow the following structure:

### Script Structure

1. **Define Constants and Parameters:**
    - `mu0`: Permeability of free space.
    - `num_points`: Number of points in each dimension for the grid.
    - `coil_radius`, `coil_center`, `frequencies`, `currents`, `phases`: Parameters defining the neurostimulation coils.

2. **Observation Grid:**
    - Define a 3D grid to simulate the brain model.

3. **Baseline Neural Activity Simulation:**
    - Simulate baseline neural activity with altered oscillatory patterns for depression.

4. **Magnetic Stimulation:**
    - Calculate the magnetic field produced by the neurostimulation coils.

5. **Post-Stimulation Neural Activity Simulation:**
    - Simulate neural activity after magnetic stimulation.

6. **Time-Varying MEG Signal Calculation:**
    - Calculate the MEG signal over time.

7. **Visualization:**
    - Plot the magnetic field slices before and after stimulation.
    - Plot the MEG signal over time.

### Major Functions Used in the Script

- **meshgrid**
    - **Usage:** `[x, y, z] = meshgrid(linspace(-0.1, 0.1, num_points), linspace(-0.1, 0.1, num_points), linspace(-0.1, 0.1, num_points));`
    - **Purpose:** Creates a 3D grid of points representing the observation space for the brain model.
- **linspace**
    - **Usage:** `linspace(-0.1, 0.1, num_points)`
    - **Purpose:** Generates linearly spaced vectors for defining the grid points in the x, y, and z dimensions.
- **sin**
    - **Usage:** `sin(2 * pi * f_beta * t(i))`
    - **Purpose:** Calculates the sine of an angle, used here to simulate oscillatory patterns in the MEG signals.
- **subplot**
    - **Usage:** `subplot(2, 2, 1);`
    - **Purpose:** Creates a subplot in a figure for plotting multiple graphs in a single window.
- **imagesc**
    - **Usage:** `imagesc(linspace(-0.1, 0.1, num_points), linspace(-0.1, 0.1, num_points), meg_baseline_slice);`
    - **Purpose:** Displays a scaled color image of the 2D matrix, used for visualizing the magnetic field slices.
- **squeeze**
    - **Usage:** `meg_baseline_slice = squeeze(meg_baseline(:, :, slice_index));`
    - **Purpose:** Removes singleton dimensions from an array, used here to extract a 2D slice from the 3D magnetic field data.
- **plot**
    - **Usage:** `plot(t, meg_baseline_time(:, slice_index), 'DisplayName', 'Baseline');`
    - **Purpose:** Plots data points in 2D space, used here to visualize the MEG signals over time.
- **hold on / hold off**
    - **Usage:** `hold on;` and `hold off;`
    - **Purpose:** Retains the current plot and certain settings so that subsequent graphing commands add to the existing graph.
- **legend**
    - **Usage:** `legend;`
    - **Purpose:** Adds a legend to the plot to label different data series.
- **title**
    - **Usage:** `title('Baseline Magnetic Field (z=0)');`
    - **Purpose:** Adds a title to the plot.
- **xlabel / ylabel**
    - **Usage:** `xlabel('x (m)');` and `ylabel('y (m)');`
    - **Purpose:** Adds labels to the x-axis and y-axis of the plot.
- **colorbar**
    - **Usage:** `colorbar;`
    - **Purpose:** Adds a color bar to the plot to indicate the color scale.
- **clim**
    - **Usage:** `clim([cmin cmax]);`
    - **Purpose:** Sets the color limits for the plot to ensure consistent color scaling across different plots.

### Generated Figures

When you run the functions, you will generate two figures. One for Parkinson’s Disease and one for Depression.
One for Parkinson's Disease looks like this:

![image](https://github.com/user-attachments/assets/7f350fd6-d85f-488f-9923-d4a7339c8cb1)

And the one for Depression looks like this:

![image](https://github.com/user-attachments/assets/f62e5526-5b6a-410e-86e1-263bbe592597)



#### Explanation of the Figures

These figures demonstrate the simulation results of neurostimulation effects on MEG signals in a simplified brain model. Here are explanations of each plot of the figures.

- **Top Row: Magnetic Field Slices**
    - **Left Plot: Baseline Magnetic Field (z=0)**
        - This plot shows the baseline magnetic field slice at the middle plane of the brain model (z=0) before any stimulation is applied.
        - The color bar indicates the strength of the magnetic field in Tesla (T), with blue regions representing negative field values and yellow regions representing positive field values.
    - **Right Plot: Post-Stimulation Magnetic Field (z=0)**
        - This plot shows the magnetic field slice at the middle plane of the brain model (z=0) after the neurostimulation has been applied.
        - The color bar again indicates the strength of the magnetic field in Tesla (T).
        - The difference between the baseline and post-stimulation plots demonstrates the effect of neurostimulation on the magnetic field.

- **Bottom Row: MEG Signal Over Time**
    - **Plot: MEG Signal Over Time**
        - This plot shows the MEG signal at the central point (slice) of the brain model over time (1 second).
        - The x-axis represents time in seconds (s), and the y-axis represents the magnetic field in Tesla (T).
        - Two lines are plotted:
            - **Blue Line (Baseline):** Represents the MEG signal before stimulation.
            - **Orange Line (Post-Stimulation):** Represents the MEG signal after stimulation.
        - The differences in amplitude and phase between the baseline and post-stimulation signals indicate how neurostimulation affects neural oscillations and activity.

#### Key Observations

- **Magnetic Field Slices:** The baseline and post-stimulation magnetic field slices show how the applied stimulation alters the magnetic field distribution within the brain model.
- **MEG Signal Over Time:** The post-stimulation MEG signal exhibits slight changes in amplitude and phase compared to the baseline, illustrating the impact of neurostimulation on neural activity. These changes can be indicative of altered neural oscillatory patterns due to stimulation.

### Statistical Analysis

Both figures look similar, and it is hard to understand if there are any differences. This is why it is important to understand statistical analysis techniques and how to use them in MATLAB. In this example, we are going to perform a t-test. Please refer to Chapter 5: Lab Example 2 for a detailed explanation on what a t-test is.

Go back to the final code in MATLAB called `ttest_rtmscoil.m` and click run.

#### Script Structure

1. **Perform t-test**
    - Use `ttest2` to compare the difference in MEG signal changes between depression and Parkinson's disease.

2. **Display Results**
    - Print the p-value, t-statistic, degrees of freedom, and conclusion about the null hypothesis based on the t-test results.

### Major Functions Used in the Script

- **ttest2**
    - **Usage:** `[~, p_value_diff, ~, stats_diff] = ttest2(meg_post(:) - meg_baseline_alpha(:), meg_post_beta(:) - meg_baseline_beta(:));`
    - **Purpose:** Performs a two-sample t-test to compare the means of two independent samples. In this script, it is used to compare the differences in MEG signals before and after stimulation between depression and Parkinson's disease conditions.
    - **Outputs:**
        - `p_value_diff`: The p-value of the t-test.
        - `stats_diff`: A structure containing the t-statistic, degrees of freedom, and other relevant information.

- **disp**
    - **Usage:** `disp(['P-value for t-test for the difference between Depression and Parkinson''s: ', num2str(p_value_diff)]);`
    - **Purpose:** Displays text or variables in the Command Window. It is used here to print the p-value, t-statistic, degrees of freedom, and conclusion about the null hypothesis.

- **num2str**
    - **Usage:** `num2str(p_value_diff)`
    - **Purpose:** Converts numbers to a string format. This is useful for concatenating numerical values with text for display purposes.

Once you have run this code, you will get some results in your Command Window.

### Explanation of the Results

The statistical analysis performed using a two-sample t-test compares the differences in the effects of neurostimulation between depression and Parkinson's disease. The results of the t-test are as follows:

- **P-value:** 0.012806
    - The p-value is a measure of the probability that the observed differences between the two conditions could have occurred by random chance. A p-value less than 0.05 is typically considered statistically significant.
    - In this case, the p-value is 0.012806, which is less than 0.05. This indicates that the differences in the effects of neurostimulation between depression and Parkinson's disease are statistically significant.

- **t-statistic:** -2.4891
    - The t-statistic is a measure of the size of the difference relative to the variation in the sample data. A larger absolute value of the t-statistic indicates a more significant difference between the groups.
    - Here, the t-statistic is -2.4891, which suggests that there is a noticeable difference between the two conditions.

- **Degrees of Freedom:** 249998
    - Degrees of freedom (df) refer to the number of independent values that can vary in the analysis. In the context of a t-test, it is used to determine the distribution of the test statistic.
    - The degrees of freedom for this test are 249998, which is typical for a large dataset.

#### Results Conclusion

Based on the p-value being less than 0.05, we reject the null hypothesis. The null hypothesis states that there is no significant difference in the effects of neurostimulation between depression and Parkinson's disease. The results indicate that there is a significant difference in how neurostimulation affects individuals with depression compared to those with Parkinson's disease.

### Conclusion

In this lab example, we explored the effects of neurostimulation on neural activity for two neurological conditions: Parkinson's disease and depression. Using MATLAB scripts, we simulated the magnetic fields and MEG signals before and after neurostimulation for both conditions, and then performed a statistical analysis to compare the differences in effects.

#### Key Findings

1. **Simulation Results**
    - The magnetic field distribution and MEG signals were visualized for both baseline and post-stimulation conditions.
    - Differences in amplitude and phase between baseline and post-stimulation MEG signals were observed, indicating the impact of neurostimulation on neural activity.

2. **Statistical Analysis**
    - A two-sample t-test was performed to statistically compare the effects of neurostimulation between depression and Parkinson's disease.
    - The p-value obtained (0.012806) was less than the significance threshold of 0.05, indicating a statistically significant difference in the effects of neurostimulation between the two conditions.
    - The t-statistic (-2.4891) further confirmed the noticeable difference, and the degrees of freedom (249998) highlighted the robustness of the analysis due to the large dataset.

#### Interpretation

The results indicate that neurostimulation affects individuals with depression differently compared to those with Parkinson's disease. This underscores the importance of tailoring neurostimulation treatments to specific neurological conditions to achieve the best therapeutic outcomes.

By combining concepts from neurostimulation, brain-computer interfaces (BCIs), and neurological disorders, this lab example provides a comprehensive understanding of how neurostimulation can modulate neural activity differently across various conditions. The statistical analysis demonstrates the importance of using quantitative methods to validate the efficacy and specificity of neurostimulation treatments, highlighting the potential for personalized therapeutic approaches in clinical practice.

Overall, this lab example serves as a practical application of theoretical knowledge, reinforcing the significance of interdisciplinary approaches in biomedical engineering and neuroscience.
