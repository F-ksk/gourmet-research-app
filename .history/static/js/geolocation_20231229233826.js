
document.addEventListener("DOMContentLoaded", function() {

    const input_location = document.getElementById("text-location")

    // ラジオボタンの初期状態によってテキストボックスの状態と背景色を設定
    if (locationRadio.checked) {
        input_location.disabled = false;
        input_location.style.backgroundColor = "white";
    } else if (currentLocationRadio.checked) {
        input_location.disabled = true;
        input_location.style.backgroundColor = "gray";
    }
    // ラジオボタンの変更イベント
    document.getElementById("location").addEventListener("change", function() {
        // 中身を空にして地名の入力フォームを有効にする
        input_location.disabled = false;
        input_location.style.backgroundColor = "white"
    });
    document.getElementById("current-location").addEventListener("change", function() {
        // 地名の入力フォームを無効にする
        //input_location.value = "";
        input_location.disabled = true;
        input_location.style.backgroundColor = "gray"
        // 位置情報を取得する
        navigator.geolocation.getCurrentPosition(successCallback, errorCallback);
    });
});
// ボタンを押した時の処理
//document.getElementById("current-location").onclick = function(){
//    // 位置情報を取得する
//    navigator.geolocation.getCurrentPosition(successCallback, errorCallback);
//};

// 取得に成功した場合の処理
function successCallback(position){
    // 緯度を取得し画面に表示
    var latitude = position.coords.latitude;
    document.getElementById("latitude").value = latitude;
    // 経度を取得し画面に表示
    var longitude = position.coords.longitude;
    document.getElementById("longitude").value = longitude;
};
    
// 取得に失敗した場合の処理
function errorCallback(error){
    alert("位置情報が取得できませんでした");
};