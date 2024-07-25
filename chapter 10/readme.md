# Chapter 10 lab 2
In this lab, we will explore Psychtoolbox and apply our knowledge through a practical task. Specifically, we will implement a working memory task inspired by the visual working memory capacity experiment conducted by *Vogel and Machizawa (2004)*. You can access the original research article at https://www.nature.com/articles/nature02447.

Psychtoolbox is a collection of free software tools that facilitates the design and implementation of precise and complex visual and auditory stimuli for psychological experiments. It is widely used in the fields of psychology, neuroscience, and vision research. Here are some key features and components of Psychtoolbox:
- Platform Compatibility: Psychtoolbox is primarily used with MATLAB and GNU Octave, making it accessible to users who prefer different programming environments.
- Stimulus Presentation: It allows for the creation and control of visual and auditory stimuli with high temporal and spatial precision. This is crucial for experiments requiring exact timing and synchronization.
- Graphics and Sound: Psychtoolbox includes functions for generating and manipulating graphics, images, and sounds. This allows researchers to create complex visual displays and auditory sequences.
- Hardware Interaction: It supports interaction with various hardware devices such as eye trackers, response boxes, and other input/output devices, enabling comprehensive experimental setups.
- Open Source: Being an open-source toolkit, Psychtoolbox is freely available and can be modified to suit specific research needs.
- Community Support: There is a strong community of users and developers who contribute to the toolbox, provide support, and share scripts and solutions.
- 
Psychtoolbox is particularly powerful in experiments that require precise control over stimulus timing and presentation, such as studies in visual perception, auditory processing, and reaction time measurement.

It is available for both MATLAB and Octave. This powerful tool offers a range of commands that simplify the process of creating experiments. For more information about the available functions, visit: Psychtoolbox Documentation. After installing Psychtoolbox in MATLAB, you can begin designing your own experiments. In this instance, we will use an implementation provided by [*Marvin Theiss*](https://github.com/mrvnthss/visual-working-memory-capacity).

## Working memory experiment

The visual working memory capacity experiment conducted by Vogel and Machizawa in 2004 aimed  to explore the limitations and neural mechanisms underpinning visual working memory. Participants in the study were presented with arrays of colored rectangles and tasked with remembering their colors and locations. Following a brief delay, they were shown a second array and had to determine if it was identical to the first or if one rectangle had changed color. The number of rectangles varied to assess memory capacity. EEG recordings, particularly focusing on the contralateral delay activity (CDA), were used to monitor neural activity. 

![image](https://github.com/user-attachments/assets/fd7a965b-8936-4db3-8404-451373a7c013)

The study found that participants' accuracy in detecting changes declined as the number of items increased, with a notable drop when the set size exceeded three to four items, indicating a memory capacity limit of about 3-4 items. Correspondingly, the amplitude of the CDA increased with the number of items up to this capacity limit, beyond which it plateaued, suggesting a fixed neural resource for visual working memory. This research highlighted that visual working memory is constrained by a capacity limit and established the CDA as a neural marker for the number of items held in memory, offering significant insights into the cognitive and neural mechanisms of working memory limitations.
Once Psychtoolbox is installed, you simply need to run the WorkingMemoryCapacity.m script. The code will first prompt participants to complete an identification form.

```Matlab
prompt = {'Participant ID (1 - 999):', ...
    'Please enter your sex (m/w/d):', ...
    'Please enter your year of birth:'};```

This allows experimenters to keep track of the data collected during the experiment. 
Additionally, the experiment provides options for adjusting specific parameters.
You can adjust the number of squares or objects to remember, as well as the total number of trials, which determines how many times the task will be repeated. In psychophysics, repeating the task is important because some effects may be too subtle to detect in just a few trials; however, repeating the task allows these effects to become more apparent when averaged over a larger number of trials.

```Matlab
% Set number of colored squares per hemifield
% NOTE: Parameters used by Vogel & Machizawa (2004): 1, 2, 3, 4, 6, 8, 10
nSquares = 4;
 
% Number of trials (excluding practice trials)
% NOTE: Vogel & Machizawa (2004) conducted 240 trials in each experiment
nTrials = 240;
 
% Number of practice trials
nPracticeTrials = 10;
```

SOA stands for "Stimulus Onset Asynchrony." It refers to the time interval between the onset of one stimulus and the onset of another stimulus. SOA is commonly used in experimental psychology, particularly in studies investigating perception, attention, and reaction times. By manipulating the SOA, researchers can examine how the timing of stimuli affects cognitive processes and behavioral responses. For example, in a visual attention experiment, varying the SOA between a cue and a target can help determine the speed and efficiency of attentional shifts.
In our case, this is variable to make the human subject unable to predict when the next stimulus happens.

```Matlab
% Set range to be used for the SOA (values are the ones used by Vogel &
% Machizawa (2004))
Duration.stimOnsetAsyncMinSecs = 0.3;  % in secs
Duration.stimOnsetAsyncMaxSecs = 0.4;  % in secs
```

Some other parameters deal with the timing of the experiment, which is crucial when getting certain results for working memory.

```Maltab
% Set remaining timing parameters for the experiment (again, values are the
% ones used by Vogel & Machizawa (2004))
Duration.arrowSecs = 0.2;              % in secs
Duration.memoryArraySecs = 0.1;        % in secs
Duration.retentionIntervalSecs = 0.9;  % in secs
Duration.testArraySecs = 2;            % in secs
```

In working memory tasks, maintaining a consistent viewing distance is crucial for several reasons. Firstly, it ensures that the visual angle of the stimuli remains constant, allowing for uniform perception across trials and participants. This consistency is essential for controlling the perceptual aspects of the task, ensuring that all stimuli appear the same size and are processed similarly by the visual system. Additionally, a proper viewing distance guarantees that stimuli are clearly visible and in focus, preventing blurriness or difficulty in distinguishing the items, which could increase cognitive load and lead to errors. Controlling the viewing distance also minimizes the need for large eye movements, reducing variability in how stimuli are processed and remembered. Large eye movements could cause some stimuli to fall outside the central part of the visual field, where visual acuity is highest, thus impairing memory encoding. Furthermore, a consistent viewing distance helps preserve the spatial relationships between stimuli, which is crucial in tasks where spatial configuration and relative positions are important for performance. Standardizing viewing distance across studies also allows for better comparison of results, enabling researchers to draw broader conclusions about visual working memory. Lastly, it helps control for variations in depth perception, ensuring that all participants experience the stimuli in a similar two-dimensional plane without unintended depth cues. Overall, maintaining an appropriate viewing distance ensures uniform perception, reduces variability, and enhances the reliability and validity of working memory research.

```Matlab
% (Orthogonal) distance from eye to screen in mm
% NOTE: This depends heavily on the setup (chair, desk, laptop vs. external
% monitor, etc.) that's being used.  With my setup, I measured the
% following distances (using a height-adjustable desk and desk chair that
% are properly adjusted to me):
%   - w/ laptop screen (MacBook Pro 16"): 550 mm
%   - w/ external monitor (Dell U4021QW 40" attached to Ergotron HX): 650 mm
viewingDistanceMM = 550;  % in mm
```

## Visual angle
Another important factor is the size of the objects to be retained in working memory. In this experiment, they subtend a visual angle of 0.65 degrees.

```Matlab
% NOTE: Vogel & Machizawa (2004) used squares with a size of 0.65° x 0.65°.
squareSizeVA = 0.65;  % in degrees of visual angle
```

Visual angle is a measure of how large an object appears to an observer, based on its size and distance from the observer. It is important in fields like vision science and experimental psychology because it helps quantify how much of the visual field an object occupies. Here's how visual angle is calculated:
### Formula for Visual Angle
The visual angle (θ) in degrees can be calculated using the formula:

$θ=2×arctan⁡(d2D)\theta = 2 \times \arctan\left(\frac{d}{2D}\right)θ=2×arctan(2Dd)$

Where:
- $θ\thetaθ$ = Visual angle in degrees
- $ddd$ = Diameter or height of the object (or stimulus)
- $DDD$ = Distance from the observer to the object
Steps for Calculation
1.	Measure the Object's Size (d): Determine the actual size of the object or stimulus in units such as centimeters or inches.
3.	Measure the Viewing Distance (D): Measure the distance from the observer’s eyes to the object or stimulus. This is often done in centimeters or inches.
4.	Apply the Formula: Substitute the values for $ddd$ and $DDD$ into the formula to find the visual angle.
### Example Calculation
Suppose you have an object that is 10 cm in diameter (d) and it is viewed from a distance of 100 cm (D).
1.	Convert the measurements into the formula:

$θ=2×arctan⁡(10/2100)=2×arctan⁡(5100)\theta = 2 \times \arctan\left(\frac{10 / 2}{100}\right) = 2 \times \arctan\left(\frac{5}{100}\right)θ=2×arctan(10010/2)=2×arctan(1005)$

2.	Calculate the visual angle:

$θ=2×arctan⁡(0.05)≈2×2.86∘≈5.72∘\theta = 2 \times \arctan(0.05) \approx 2 \times 2.86^\circ \approx 5.72^\circθ=2×arctan(0.05)≈2×2.86∘≈5.72∘$

So, the visual angle of the object is approximately 5.72 degrees.
## Subject responses
Participants are asked to respond if they notice a change in the square configuration, indicating whether the pattern is identical or different. Psychtoolbox uses specific code to facilitate response mechanisms, such as the keyboard. In this case, pressing the letter 'J' signifies that the pattern is identical, while pressing 'F' indicates that it is different.

```Matlab
% Set keys
% NOTE: The space bar will be used by participants to navigate through
% instructions.  To indicate a decision, participants will press either 'J'
% (indicating identical arrays) or 'F' (indicating different arrays).
% Finally, the escape key can be used to prematurely end the experiment.
Key.space = KbName('SPACE');
Key.identical = KbName('J');
Key.different = KbName('F');
Key.escape = KbName('ESCAPE');
```
The response is then logged after every trial of the experiment

```Matlab
%   7.2 Store participant's response
        trials.Response(iTrial) = response;
```
The responses, along with the data from each trial, are then saved in an Excel file.

![image](https://github.com/user-attachments/assets/8770c24d-1b11-43b1-9eb4-7a4c3bce16d9)

The package from Marvin Theiss also includes a procedure for analyzing the data generated from the experiment. This script processes the CSV file created during the experiment and calculates the hit rate, false alarm rate, and working memory capacity.
In working memory tasks, capacity is typically calculated using the measure "K," which represents the number of items a participant can hold in working memory. This measure is often derived from a change detection task where participants are shown an array of visual stimuli, such as colored rectangles, for a brief period. After a short delay, a second array is presented, and participants must determine if it is the same as the first array or if one item has changed. The number of items in the arrays, or set size, varies across trials. To calculate K, the proportion of correct responses (hit rate) and incorrect responses when no change occurs (false alarm rate) are recorded. The formula for calculating working memory capacity is $K=S×(H−F)K = S \times (H - F)K=S×(H−F)$, where S is the set size, H is the hit rate, and F is the false alarm rate. For example, with a set size of 4 items, a hit rate of 0.75, and a false alarm rate of 0.20, the capacity K would be $4×(0.75−0.20)=2.24 \times (0.75 - 0.20) = 2.24×(0.75−0.20)=2.2$. This means the participant can accurately maintain and process about 2.2 items in their visual working memory. This calculation is essential for understanding individual differences in cognitive abilities and comparing performance across different populations or experimental conditions.

![image](https://github.com/user-attachments/assets/a6004ae7-692b-4abe-ab41-439ac26b4cfd)

In our case, the capacity is approximately 3.4, this means that, on average, the participant (us) can hold and accurately maintain about 3.4 items in their visual working memory. This measure indicates the maximum number of items a person can effectively store and manipulate in their mind over a short period.
### Implications of a Capacity of 3.4
1.	**High Performance**:
o	A capacity of 3.4 is relatively high, suggesting that participants have a strong ability to retain and process visual information.
2.	**Comparison to Typical Capacities:**
o	This value is above the commonly cited average working memory capacity of 3-4 items, indicating that participants are performing at or slightly above average in terms of their visual working memory abilities.
3.	**Experimental Context**:
o	This capacity is context-dependent and can be influenced by various factors such as the nature of the stimuli, the duration of the retention interval, and the specific task demands.
4.	**Cognitive Implications**:
o	Higher working memory capacity is often associated with better performance in tasks that require attention, problem-solving, and learning. It suggests that participants can efficiently manage and utilize multiple pieces of visual information simultaneously.
A working memory capacity of approximately 3.4 means that participants are capable of holding and accurately recalling around 3.4 visual items at a time, reflecting a robust capacity for visual information processing. This measure provides valuable understanding into their cognitive abilities and can inform further research or practical applications where working memory plays a crucial role.
The most common capacity for visual working memory, often cited in psychological and cognitive neuroscience research, is typically around 3-4 items. This estimate is based on numerous studies that have investigated the limits of working memory using various tasks and methodologies.
## Evidence about capacity (K)
1.	**Classic Studies**: Early research by George Miller in 1956 suggested that the average capacity of short-term memory is about 7 ± 2 items. However, more recent studies focusing specifically on visual working memory have found that this capacity is actually smaller, generally around 3-4 items.
2.	**Empirical Findings**: Many experiments using change detection tasks, similar to the ones described by Vogel and Machizawa (2004), consistently find that participants can hold approximately 3-4 items in visual working memory before their performance begins to decline.
3.	**Contralateral Delay Activity (CDA)**: Research using neural measures such as CDA also supports this capacity limit. The CDA amplitude increases with the number of items held in memory up to about 3-4 items, after which it plateaus, indicating a maximum capacity.
   
# We invite you to complete this task to determine your own working memory capacity.

## References
Brainard, D. H. (1997). The Psychophysics toolbox. Spatial Vision, 10(4), 433–436. https://doi.org/10.1163/156856897X00357

Kleiner, M., Brainard, D. H., & Pelli, D. G. (2007). What’s new in Psychtoolbox-3? Perception, 36(ECVP Abstract Supplement), 14. https://doi.org/10.1177/03010066070360S101

Pavlov, Y. G., Adamian, N., Appelhoff, S., Arvaneh, M., Benwell, C. S. Y., Beste, C., Bland, A. R., Bradford, D. E., Bublatzky, F., Busch, N. A., Clayson, P. E., Cruse, D., Czeszumski, A., Dreber, A., Dumas, G., Ehinger, B., Ganis, G., He, X., Hinojosa, J. A., … Mushtaq, F. (2021). #EEGManyLabs: Investigating the replicability of influential EEG experiments. Cortex, 144, 213–229. https://doi.org/10.1016/j.cortex.2021.03.013

Pelli, D. G. (1997). The VideoToolbox software for visual psychophysics: Transforming numbers into movies. Spatial Vision, 10(4), 437–442. https://doi.org/10.1163/156856897X00366

The MathWorks Inc. (2023). MATLAB (9.14.0) [Computer software]. The MathWorks Inc. https://www.mathworks.com

Vogel, E. K., & Machizawa, M. G. (2004). Neural activity predicts individual differences in visual working memory capacity. Nature, 428(6984), 748–751. https://doi.org/10.1038/nature02447

## Acknowledgments
- The experiment code is based on the Psychtoolbox library. For more information about Psychtoolbox, visit Psychtoolbox.
- The grammarly.com Grammar Checker was used to check written text for spelling and grammar mistakes.
- Screenshots and screen capture videos were taken/recorded using macOS' built-in Screenshot app.
- The Gifski app was used to convert screen capture videos into GIFs.
