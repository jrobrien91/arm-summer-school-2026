# 2026 ARM Big Open Data Summer School

**Monday, May 18, to Friday, May 22, 2026**

The “Big Open Data Science Summer School” is geared toward students from undergraduates to early postdoctoral scholars. Planned activities include instructional talks, tutorials, and a mentored hackathon for attendees to work with ARM data and open-source software.

![SGP-Photo](/images/figures/Summer_school_2026.jpg)

## Mission
The overarching mission of the summer school is to enhance the scientific impact of ARM observations through the instruction of students in new techniques to gain insight into atmospheric processes using open science tools.

## Objectives
- increase knowledge about the range of ARM observations, demonstrate innovative and methodologically sound use of those observations, and connect students to a variety of knowledgeable resources (e.g., ARM instrument mentors)

- introduce students to resources within ARM for high performance data-proximate computation

- equip students with a variety of techniques for comparing high-resolution model output with ARM observations to study a range of atmospheric processes

- apply artificial intelligence techniques to ARM data applications.

## Organizers
| Name     | Affiliation | Links   |
| :------- | ----------- |:------- |
| Scott Collis | Argonne National Laboratory | [Github](https://github.com/scollis) |
| Joseph O'Brien | Argonne National Laboratory | [Github](https://github.com/jrobrien91) |
| Jeri Knepper | Argonne National Laboratory | |

## Instructors and Mentors

| Instructor | Affiliation | Links |
| :------- | ------- |:------- |
| Mark Spychala  | Argonne National Laboratory           | [Github](https://github.com/Metspy) |
| Adam Theisen   | Argonne National Laboratory           | [Github](https://github.com/AdamTheisen) |
| Robert Jackson | Argonne National Laboratory           | [Github](https://github.com/rcjackson) |
| Bhupendra Raut | Argonne National Laboratory           | [Github](https://github.com/RBhupi) |
| Bill Gustafson | Pacific Northwest National Laboratory | [Github](https://github.com/wgustafson) |
| Alyssa Sockol  | University of Oklahoma/CIWRO          | [Github](https://github.com/ajsockol) |
| Maria Cadeddu  | Argonne National Laboratory           |  |
| Connor Flynn   | University of Oklahoma                | [Github](https://github.com/ConnorJFlynn) |
| Hsi-Yen Ma     | Lawrence Livermore National Laboratory | [Github](https://github.com/hyma68) |
| Andrew Dzambo  | CIWRO                                 |  | 

## Running on Your Own Machine
If you are interested in running this material locally on your computer, you will need to follow this workflow:

1. Clone the [2026 ARM Summer School](https://github.com/ARM-Development/arm-summer-school-2026) repository:

   ```bash
    git clone https://github.com/ARM-Development/arm-summer-school-2026
    ```  
1. Move into the `arm-summer-school-2026` directory
    ```bash
    cd arm-summer-school-2026
    ```  
1. Create and activate your conda environment from the `environment.yml` file
    ```bash
    conda env create -f environment.yml
    conda activate arm-summer-school-2026-dev
    ```  
1.  Move into the `notebooks` directory and start up Jupyterlab
    ```bash
    cd notebooks/
    jupyter lab
    ```