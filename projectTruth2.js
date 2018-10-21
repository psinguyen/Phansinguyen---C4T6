var truth = document.querySelector(".clean-mtop-mbot")
var truthQuest=[
    "Một tuần xem phim XXX bao nhiêu lần ?",
    "Who do you find most attractive in this room?",
    "What would you do if you lived in the body of someone of the opposite sex for one day?",
    "What is the most shameful thing you've done in your life? ",
    "Who did you have your best kiss with",
    "Have you ever been so high or drunk that you were speaking with objects?",
    "If you make your phone or keys fall in the toilets, would you put your hand in it to get it back?",
    "What is the worst thing you've ever done to somebody?",
    "Have you ever had a crush on someone that your best friend has dated?",
    "Who's the most inappropriate person you've ever fantasized about?",
    "What's the strangest place in which you've had sex?",
    "Would you sleep with someone for a promotion?",
    "What's the craziest thing you've ever done in bed?",
    "What do you find the most disgusting about the opposite sex?",
    "Could you have sex with someone of the same gender?",
    "Were you turned on the first time you met your crush?",
    "Have you ever had sex in the swimming pool/the sea?",
    'What part of your body are you the proudest of?',
    "Have you ever paid for sex?",
    "What limits you can't cross in bed?"
]
var choiceRandom = () => {
    
    var index = Math.floor(Math.random() * truthQuest.length);
       
    return truthQuest[index];
}
var choiceRandomed = choiceRandom();
truth.innerHTML = choiceRandomed;

var clicks = document.querySelectorAll(".click");
// var clicks = document.querySelectorAll(".click2");
clicks.forEach(clicks => {
    clicks.addEventListener("click", (event) => {
        if (clicked === choiceRandomed) {
            document.querySelectorAll(".clean-mtop-mbot")
                
            }
        else {
                console.log(truthQuest);
                
            }
            
        })
    
    
});
var otherQuestion = () =>{
    var choiceRandomed = choiceRandom();
    truth.innerHTML = choiceRandomed;
    for (var i = 0;i < truthQuest.length; i++){
        truthQuest[i].style.backgroundColor = truthQuest[i];
        
}
}
window.addEventListener("click",()=>{
    otherQuestion();
})
