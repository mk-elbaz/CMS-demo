document.addEventListener("DOMContentLoaded", function () {
    const filledStar = "M3.612 15.443c-.386.198-.824-.149-.746-.592l.83-4.73L.173 6.765c-.329-.314-.158-.888.283-.95l4.898-.696L7.538.792c.197-.39.73-.39.927 0l2.184 4.327 4.898.696c.441.062.612.636.282.95l-3.522 3.356.83 4.73c.078.443-.36.79-.746.592L8 13.187l-4.389 2.256z"
    const emptyStar = "M2.866 14.85c-.078.444.36.791.746.593l4.39-2.256 4.389 2.256c.386.198.824-.149.746-.592l-.83-4.73 3.522-3.356c.33-.314.16-.888-.282-.95l-4.898-.696L8.465.792a.513.513 0 0 0-.927 0L5.354 5.12l-4.898.696c-.441.062-.612.636-.283.95l3.523 3.356-.83 4.73zm4.905-2.767-3.686 1.894.694-3.957a.565.565 0 0 0-.163-.505L1.71 6.745l4.052-.576a.525.525 0 0 0 .393-.288L8 2.223l1.847 3.658a.525.525 0 0 0 .393.288l4.052.575-2.906 2.77a.565.565 0 0 0-.163.506l.694 3.957-3.686-1.894a.503.503 0 0 0-.461 0z"

    let ratingCounter = 1;

    const tutorName = document.querySelector("#tutorName").innerHTML

    const starOne = document.querySelector("#starOne")
    const starOneP = document.querySelector("#starOneP")
    const starTwo = document.querySelector("#starTwo")
    const starTwoP = document.querySelector("#starTwoP")
    const starThree = document.querySelector("#starThree")
    const starThreeP = document.querySelector("#starThreeP")
    const starFour = document.querySelector("#starFour")
    const starFourP = document.querySelector("#starFourP")
    const starFive = document.querySelector("#starFive")
    const starFiveP = document.querySelector("#starFiveP")


    const submitRate = document.querySelector("#submitRate")
    
    starOne.addEventListener("click", ()=> {
        ratingCounter = 1
        starTwoP.setAttribute('d',emptyStar)
        starThreeP.setAttribute('d',emptyStar)
        starFourP.setAttribute('d',emptyStar)
        starFiveP.setAttribute('d',emptyStar)
    })

    starTwo.addEventListener("click", ()=> {
        ratingCounter = 2
        starTwoP.setAttribute('d',filledStar)
        starThreeP.setAttribute('d',emptyStar)
        starFourP.setAttribute('d',emptyStar)
        starFiveP.setAttribute('d',emptyStar)
    })

    starThree.addEventListener("click", ()=> {
        ratingCounter = 3
        starTwoP.setAttribute('d',filledStar)
        starThreeP.setAttribute('d',filledStar)
        starFourP.setAttribute('d',emptyStar)
        starFiveP.setAttribute('d',emptyStar)
    })

    starFour.addEventListener("click", ()=> {
        ratingCounter = 4
        starTwoP.setAttribute('d',filledStar)
        starThreeP.setAttribute('d',filledStar)
        starFourP.setAttribute('d',filledStar)
        starFiveP.setAttribute('d',emptyStar)

    })

    starFive.addEventListener("click", ()=> {
        ratingCounter = 5
        starTwoP.setAttribute('d',filledStar)
        starThreeP.setAttribute('d',filledStar)
        starFourP.setAttribute('d',filledStar)
        starFiveP.setAttribute('d',filledStar)
    })

    submitRate.addEventListener("click", ()=> {
        const csrftoken = getCookie("csrftoken");

        fetch("/submitRate", {
            method: "POST",
            headers: {
              "X-CSRFToken": csrftoken,
            },
            body: JSON.stringify({
              tutor : tutorName,
              rate : ratingCounter
            }),
          })
            .then((response) => response.json())
            .then((result) => {
              // Print result
              console.log(result);
              alert(result.message)

            })
            .catch((error) => {
              console.log(error)
              alert(error.error)
            });

            window.location.href = 'http://127.0.0.1:8000/getSubjects';

    })
});


function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(";").shift();
  }