#!/usr/bin/perl
use strict;

# for (my $d=1;$d<=1000;$d++){
# 	print "$d\t".(i2s($d))."\n";
# }

# for (my $d=1000;$d<=1000000;$d=$d+999){
# 	print "$d\t".(i2s($d))."\n";
# }

for (my $d=1000000;$d<=999000000;$d=$d+999999){
	print "$d\t".(i2s($d))."\n";
}

# my $d = 918999082;
# print "$d\t".(i2s($d))."\n";

sub i2s{
	my $out = '';
	my @base = ('','один','два','три','четыре','пять','шесть','семь','восемь','девять');
	my @ebase = ('','одна','две');
	my @hbase = ('','сто','двести','триста','четыреста','пятьсот','шестьсот','семьсот','восемьсот','девятьсот');
	my @dbase = ('','десять','двадцать','тридцать','сорок','пятьдесят','шестьдесят','семьдесят','восемьдесят','девяносто');
	my @abase = ('десять','одиннадцать','двенадцать','тринадцать','четырнадцать','пятнадцать','шестнадцать','семнадцать','восемнадцать','девятнадцать');
	my @sel = ('','тысяч','миллио','');

	my ($tag,$sec_tag, $count,$ch,$t,$index,$tree);

	my($i)=(@_);
	my ($len) = length ($i)-1;
	for $tree (0..($len/3)){
		$t = ''; 
		for $count (0..2){
			$index = $count + $tree*3;
			if ( $index <= $len){
				$ch = substr ($i,$len - $index,1);
				if ($count == 0){
					$tag = $ch;
					if ($tree == 1 && ($ch == 1 || $ch == 2 )){
						$t = $ebase[$ch] . ' ' . $t;
					}else { 
						$t = $base[$ch] . ' ' . $t; 
					}
				}elsif ( $count == 1){
					$sec_tag = $ch;
					if ($ch != 1){
						$t = $dbase[$ch] . ' ' . $t ; 
					}else{
						$t = $abase[$tag]; 
					} 
				}else{
					$t = $hbase[$ch] . ' ' . $t; 
				}
			}
		}
		my $ok = "";
		if ($tree eq '1'){
			if ($sec_tag != 1){
				if ($tag eq '1'){
					$ok = "а";
				}elsif( $tag >=2 && $tag <=4){
					$ok = "и";
				}
			}else{
				if ($tag eq '1'){
					$ok = "а";
				}elsif($tag eq '2' || $tag eq '3' || $tag eq '4'){
					$ok = "и";
				}
			}
		}elsif ($tree eq '2'){
			if ($sec_tag != 1){
				if ($tag eq '1'){
					$ok = "н";
				}elsif( $tag >=2 && $tag <=4){
					$ok = "на";
				}else{
					$ok = "нов";
				}
			}else{
				if ($tag eq '1'){
					$ok = "а";
				}elsif($tag eq '2' || $tag eq '3' || $tag eq '4'){
					$ok = "нов";
				}else{
					$ok = "нов";
				}
			}
		}
		if ($t !~ /^\s*$/){
			$out = $t . ' ' . $sel[$tree].$ok. ' ' . $out  ;
		}
	}

	# $out = rusUc($out);
	$out =~ s/\s{2,}/ /g;
	return $out;
}


1;