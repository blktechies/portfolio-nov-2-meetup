#!/usr/bin/env php
<?php
   /** 
    * Portfolio and prices problem for the 
    * November 2, 2011 Black Techies Meetup.
    *
    * (It's really ugly!)
    * @author Kyle Wanamaker
    * @date 2011-11-02
    **/



try {
  $f = fopen('data/portfolio.dat', 'r');
  $p = fopen('data/prices.dat', 'r');
} catch (Exception $e) {
  printf(STDERR, "Could not open file for writing");
}

$portfolio = array();
$start_value = 0.0;
$end_value = 0.0;

while($l = fgets($f)){
  $entry = preg_split('/\s+/', $l);
  $portfolio[$entry[0]][] = array( 
		       'qty' => $entry[1],
		       'price' => (float) $entry[2],
			);
}

foreach($portfolio as $ticker) {
  foreach($ticker as $book_entry) {
    $start_value += (float) $book_entry['qty'] * $book_entry['price'];
  }
}

while($l = fgets($p)){
  $entry = preg_split('/\s+/', $l);
  if( isset($portfolio[$entry[0]])){
    foreach($portfolio[$entry[0]] as $book_entry){
      $end_value += $book_entry['qty'] * $entry[1];
    }
  }
}
printf("Starting value: %.2f\n", $start_value);
printf("End value: %.2f\n", $end_value);
printf("Portfolio delta: %.2f %s\n", 
       ($delta = $end_value - $start_value),
       $delta > 0 ? ':)' : ':(' ); 


