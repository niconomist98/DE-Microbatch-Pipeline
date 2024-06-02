## DE-Microbatch-Pipeline
Custom pipeline for microbatch data ingestion into sqlite3 database applying file-by-file, line-by-line  ingestion with near real time stats tracking and updating

<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->
Please check the folder "Files" , there you'll find the initial testing notebooks
![image](https://github.com/niconomist98/DE-Microbatch-Pipeline/assets/105328047/d72ebe4e-7faf-4f24-b0ca-a6b642ed5edc)

Modularized code can be found in "pipeline" folder and main.py file 
![image](https://github.com/niconomist98/DE-Microbatch-Pipeline/assets/105328047/2838ed39-d1cb-4c42-a5d8-5b477d93afed)



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->


<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="https://miro.medium.com/v2/resize:fit:594/1*MLFxdoY6ImiTghX9l0lDTA.png" alt="Logo" width="250" height="250">
    <img src="https://ojt.com/wp-content/uploads/2021/08/python-programming-language.png" alt="Logo" width="250" height="250">
    <img src="https://pythondiario.com/wp-content/uploads/2013/12/sqlite.png" alt="Logo" width="250" height="250">
  </a>
  <h3 align="center">DE-Microbatch-Pipeline
</h3>

  <p align="center">
  Microbatch , near real time processing pipeline, containeraized for easy replication and review in data engineering projects

</div>




<!-- ABOUT THE PROJECT -->




<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Installation
Pull the docker image 
  ```sh
  docker pull niconomist98/pragma-microbatch-pipeline
  ```
Run the pipeline with the docker container
  ```sh
  docker run niconomist98/pragma-microbatch-pipeline
  ```


<!-- USAGE EXAMPLES -->
## Usage

* Run the docker image and the pipeline will start its workflow, the pipeline contains a preprocessing step to handle missing values in raw data before ingestion

  ![image](https://github.com/niconomist98/DE-Microbatch-Pipeline/assets/105328047/cb0a0d35-be63-44a0-8eb5-e526c35292cd)
  
  ![image](https://github.com/niconomist98/DE-Microbatch-Pipeline/assets/105328047/452e69ee-ee5e-489b-86d4-e999d884570d)

* Once preprocessing is completed, the pipeline starts ingestion, inserting line by line and updating the stats of average price, min, max and row counts without querying the final sqlite3 table, updating these calculations in near real time

   ![image](https://github.com/niconomist98/DE-Microbatch-Pipeline/assets/105328047/9546159b-4999-48a3-b1cb-83aabca8ec1f)

* Once mini batch ingestion is completed, the pipeline run queries against the sqlite3 prices table (final table after ingestion) to verify the stats report of avg min, max, count of price column
  
    ![image](https://github.com/niconomist98/DE-Microbatch-Pipeline/assets/105328047/27625b2d-dcc1-4e5a-b645-14b8f86cd406)

* Once the general datasets pipeline is completed, the process starts once again, runing the pipeline for validation dataset, preprocessing data to handle null values, inserting one by one in database updating the stats in real time and querying the final table to validate the results
  
   ![image](https://github.com/niconomist98/DE-Microbatch-Pipeline/assets/105328047/a4772fff-2471-442e-9a0b-0315f6591c12)


    ![image](https://github.com/niconomist98/DE-Microbatch-Pipeline/assets/105328047/f4438c95-c351-4cd3-b049-5d61c767a926)

<p align="right">(<a href="#readme-top">back to top</a>)</p>




<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact
Nicolas Restrepo Carvajal
https://www.linkedin.com/in/niconomist98/

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
