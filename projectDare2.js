dare = document.querySelector(".clean-mtop-mbot")
var dareQuest = [
    "Hét to Crush của tôi là ... và tôi muốn làm với cô/anh ấy",
    "Hôn lên môi người chơi khác giới với bạn",
    "Thẩm du trước mặt mọi người",
    "Hít bất kì thứ gì của 1 người chơi bất kì",
    "Tỏ tình 1 người do người chơi khác chọn ",
    "Bị 1 người chơi bất kì búng mạnh vào bộ phận sinh dục 10 phát",
    "Chống đẩy 100 cái",
    "Thực hiện động tác 'trồng cây chuối' trong 120 giây",
    "Ngậm mù tạt trong miệng 1 phút",
    "Đối với nam thì trang điểm . Còn nữ thì tẩy trang",
    "Thả 1 vật được chỉ định vào trong bồn cầu rồi dùng tay không lấy vật đó ra",
    "Múa quạt trong 1 phút",
    "Cởi quần trong 5 phút",
    "Liếm bàn",
    "Ăn 2 thìa mù tạt",
    "Gọi điện cho Crush và nói rằng 'I love you ' ",
    "Hôn vào má hoặc môi của người chơi cùng giới ",
    "Cho đá lạnh vào trong underpants",
    "Người chơi khác sẽ chỉnh sửa kiểu tóc cho bạn",
    "Nhảy sexy dance trong 1 phút",
    

];
var choiceRandom = () => {
    
    var index = Math.floor(Math.random() * dareQuest.length);
       
    return dareQuest[index];
}
var choiceRandomed = choiceRandom();
dare.innerHTML = choiceRandomed;

// var clicks = document.querySelectorAll(".click");
var clicks = document.querySelectorAll(".click2");
clicks.forEach(clicks => {
    clicks.addEventListener("click", (event) => {
        if (clicked === choiceRandomed) {
            document.querySelectorAll(".clean-mtop-mbot")
                
            }
        else {
                console.log(dareQuest);
                
               
               
                
            }
            
        })
    
    
});
var otherQuestion = () =>{
    var choiceRandomed = choiceRandom();
    dare.innerHTML = choiceRandomed;
    for (var i = 0;i < dareQuest.length; i++){
        dareQuest[i].style.backgroundColor = dareQuest[i];
        



}
}
window.addEventListener("click",()=>{
    otherQuestion();
    
})