# Chapter 10: Lab Example 1

## Overview
This lab exercise aims to introduce students to virtual reality (VR) in psychophysics research by interacting with a simple VR world using MATLAB. The exercise will guide students through loading a VRML (Virtual Reality Modeling Language) world, opening it in a VR viewer, and interacting with basic objects within the VR environment.

## Requirements
- MATLAB software
- Virtual Reality Toolbox
- VRML world file (`simple_world.wrl`)
- Provided MATLAB code

## Part 1: Setting Up the VR Environment

### Step 1: Preparing MATLAB
Ensure the MATLAB Virtual Reality Toolbox is installed and configured on your system.

### Step 2: Creating the VRML World

Create a simple VRML world file (`simple_world.wrl`). This file should contain basic objects such as a table and a ball.

`simple_world.wrl`:

```wrl
VRML V2.0 utf8
WorldInfo {
  title "Simple World"
}

Background {
  skyColor [0.8 0.8 1.0]
}

Transform {
  translation 0 0 0
  children [
    Shape {
      geometry Box { size 4 0.2 4 }
      appearance Appearance {
        material Material { diffuseColor 0.8 0.1 0.1 }
      }
    }
    Transform {
      translation 0 1 0
      children [
        Shape {
          geometry Sphere { radius 0.5 }
          appearance Appearance {
            material Material { diffuseColor 1 1 1 }
          }
        }
      ]
    }
  ]
}
```

## Part 2: Interacting with the VRML World in MATLAB

### Step 3: Loading the VRML World

Use the provided MATLAB code to load and open the VRML world in a VR viewer.

```matlab
% Load the VRML world
vrWorld = vrworld('simple_world.wrl');

% Open the VRML world
open(vrWorld);

% Create a viewer window for the VRML world
vrFigure = vrfigure(vrWorld);
```

### Step 4: Running the Code
1. Save the provided VRML code in a file named `simple_world.wrl`.
2. Open MATLAB and navigate to the directory containing `simple_world.wrl`.
3. Copy and paste the MATLAB code into the MATLAB command window or a script file.
4. Run the MATLAB code to load the VRML world and open the VR viewer.

### Step 5: Exploring the VR Environment
Interact with the VRML world using the VR viewer controls. The VR world should look like the image provided, featuring a simple setup with a red table and a white ball on top of it against a light blue background.

Observe the simple objects (table and ball) and their properti es. 






## Part 3: Experimentation

### Step 6: Modifying the VRML World
Modify the `simple_world.wrl` file to change the properties of the objects (e.g., color, size, position). Reload the VRML world in MATLAB to see the changes.

### Step 7: Recording Observations
Note how different properties of the objects (such as size and color) affect your perception in the VR environment. Consider the potential applications of VR in psychophysical experiments, such as studying the perception of size, color, and spatial relationships.

## Conclusion
This lab exercise introduced you to the basics of using VR in psychophysics research. You learned how to create a simple VRML world, load it into MATLAB, and interact with it using a VR viewer. By modifying the VR environment and observing the changes, you gained insights into the potential applications of VR for studying sensory perception.

## Further Reading
- MATLAB Documentation on Virtual Reality Toolbox: [MATLAB VR Toolbox](https://www.mathworks.com/help/sl3d/)
- VRML and X3D Specifications: [Web3D Consortium](https://www.web3d.org/)

