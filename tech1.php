<?
function read($filename){
	if(file_exists($filename)){
		return file_get_contents($filename);
	} else {
		return false;
	}
}

function format_portfolio($portfolio, $offset = 0){
	$portfolio = explode("\n", $portfolio);
	$r = array();
	foreach($portfolio as $stock){
		if(!empty($stock)){
			$stock = explode(" ", $stock);		
			$r[$stock[0]]['q']=$stock[1];
			$r[$stock[0]]['p']=$stock[2];
			unset($portfolio[$i]);
		}
	}
	return $r;
}

function format_prices($prices, $offset = 1){
	$prices = explode("\n", $prices);
	$r = array();
	foreach($prices as $price){
		if(!empty($price)){
			$price = explode(" ", $price);		
			$r[$price[0]]['p']=$price[1];
		}
	}
	return $r;
}

function get_value_change($portfolio, $prices){
	foreach($portfolio as $symbol=>$stock){
		$portfolio[$symbol]['d']=($portfolio[$symbol]['p']-$prices[$symbol]['p'])*$portfolio[$symbol]['q'];
	}
	return $portfolio;
}

$portfolio = format_portfolio(read('/Users/steven/Desktop/meetup/portfolio.dat'));
$prices = format_prices(read('/Users/steven/Desktop/meetup/prices.dat'));
$changes = get_value_change($portfolio, $prices);
foreach($changes as $stock=>$datum){
	echo $stock." ".$datum['d'].PHP_EOL;
}
?>
