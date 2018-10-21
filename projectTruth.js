var truth = document.querySelector(".clean-mtop-mbot")
var truthQuest=[
    "Bạn có muốn đấm GVCN không ?",
    "Lý do bạn mất gốc Hóa ?",
    "Bạn thích nhất điều gì ở người bạn đang nói chuyện cùng",
    "Giấc mơ kỳ cục nhất bạn từng mơ",
    "Một điều gì bạn muốn thay đổi về bản thân mình",
    "Một câu đùa mà bạn thấy hài hước nhất",
    "Nếu một ngày tỉnh dậy bạn có thể tàng tình, thì bạn sẽ làm gì",
    "Bạn có muốn nổi tiếng không? Theo cách nào?",
    "Điều gì tạo nên một ngày “hoàn hảo” đối với bạn?",
    "Bạn có bất kì linh cảm bí mật nào về cách mà mình sẽ chết?",
    "Nêu lên 3 thứ là điểm chung của bạn và người bạn của mình.",
    "Điều gì khiến bạn cảm thấy biết ơn trong cuộc đời mình?",
    "Thành tích tuyệt vời nhất của bạn là gì?",
    "Điều gì mà bạn quý trọng nhất trong tình bạn?",
    "Kỉ niệm quý giá nhất của bạn là gì?",
    "Kỉ niệm kinh khủng nhất của bạn là gì?",
    "Tình bạn có ý nghĩa như thế nào với bạn?",
    "Điều gì, nếu có, là quá quan trọng để bị đem là làm trò đùa?",
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
