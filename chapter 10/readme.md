## Chapter 10 lab 2
In this lab, we will explore Psychtoolbox and apply our knowledge through a practical task. Specifically, we will implement a working memory task inspired by the visual working memory capacity experiment conducted by Vogel and Machizawa (2004). You can access the original research article at https://www.nature.com/articles/nature02447.- 
Psychtoolbox is a collection of free software tools that facilitates the design and implementation of precise and complex visual and auditory stimuli for psychological experiments. It is widely used in the fields of psychology, neuroscience, and vision research. Here are some key features and components of Psychtoolbox:
- 1.	Platform Compatibility: Psychtoolbox is primarily used with MATLAB and GNU Octave, making it accessible to users who prefer different programming environments.
- 2.	Stimulus Presentation: It allows for the creation and control of visual and auditory stimuli with high temporal and spatial precision. This is crucial for experiments requiring exact timing and synchronization.
- 3.	Graphics and Sound: Psychtoolbox includes functions for generating and manipulating graphics, images, and sounds. This allows researchers to create complex visual displays and auditory sequences.
- 4.	Hardware Interaction: It supports interaction with various hardware devices such as eye trackers, response boxes, and other input/output devices, enabling comprehensive experimental setups.
- 5.	Open Source: Being an open-source toolkit, Psychtoolbox is freely available and can be modified to suit specific research needs.
- 6.	Community Support: There is a strong community of users and developers who contribute to the toolbox, provide support, and share scripts and solutions.
Psychtoolbox is particularly powerful in experiments that require precise control over stimulus timing and presentation, such as studies in visual perception, auditory processing, and reaction time measurement.
It is available for both MATLAB and Octave. This powerful tool offers a range of commands that simplify the process of creating experiments. For more information about the available functions, visit: Psychtoolbox Documentation. After installing Psychtoolbox in MATLAB, you can begin designing your own experiments. In this instance, we will use an implementation provided by Marvin Theiss.

[https://github.com/mrvnthss/visual-working-memory-capacity](https://github.com/mrvnthss/visual-working-memory-capacity)

![image](https://github.com/user-attachments/assets/fd7a965b-8936-4db3-8404-451373a7c013)

The visual working memory capacity experiment conducted by Vogel and Machizawa in 2004 aimed  to explore the limitations and neural mechanisms underpinning visual working memory. Participants in the study were presented with arrays of colored rectangles and tasked with remembering their colors and locations. Following a brief delay, they were shown a second array and had to determine if it was identical to the first or if one rectangle had changed color. The number of rectangles varied to assess memory capacity. EEG recordings, particularly focusing on the contralateral delay activity (CDA), were used to monitor neural activity. The study found that participants' accuracy in detecting changes declined as the number of items increased, with a notable drop when the set size exceeded three to four items, indicating a memory capacity limit of about 3-4 items. Correspondingly, the amplitude of the CDA increased with the number of items up to this capacity limit, beyond which it plateaued, suggesting a fixed neural resource for visual working memory. This research highlighted that visual working memory is constrained by a capacity limit and established the CDA as a neural marker for the number of items held in memory, offering significant insights into the cognitive and neural mechanisms of working memory limitations.
Once Psychtoolbox is installed, you simply need to run the WorkingMemoryCapacity.m script. The code will first prompt participants to complete an identification form.

`prompt = {'Participant ID (1 - 999):', ...

    'Please enter your sex (m/w/d):', ...
    
    'Please enter your year of birth:'};
`
