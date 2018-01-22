<?php

include('simple_html_dom.php');
if(isset($_POST['submit'])){ // Fetching variables of the form which travels in URL
$url = $_POST['url'];
$target = $_POST['lang'];

$html = file_get_html($url);

foreach($html->find('p') as $e) {
    $content= $e->innertext;



$api_key = 'AIzaSyD57eC4GMivU6wRW6p2127RzsztTPip7yE';
$source="en";


$url = 'https://www.googleapis.com/language/translate/v2?key=' . $api_key . '&q=' . rawurlencode($content);
$url .= '&target='.$target;
$url .= '&source='.$source;

$response = file_get_contents($url);
$obj =json_decode($response,true); //true converts stdClass to associative array.


if($obj != null)
{
    if(isset($obj['error']))
    {
        echo "Error is : ".$obj['error']['message'];
    }
    else
    {   echo"<p>".$obj['data']['translations'][0]['translatedText']."</p>";
    }
}
else
    echo "UNKNOWN ERROR";

}
}

?>
