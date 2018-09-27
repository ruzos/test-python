# Program wielokrotnie rozgaleziony

print "Ten program przewidzi Twoja dlugosc zycia"

odp = raw_input("Czy palisz papierosy?")

if odp == "Tak" or odp == "TAK" or odp == "tak" or odp == "no pewnie":

    odp = raw_input ("A czy sie zaciagasz?")

    if odp == "Tak" or odp == "TAK" or odp == "tak" or odp == "no pewnie":

        print "Nie pozyjesz dlugo!"

    else:

        print "To pozyjesz dlugo!"

else:

    print "Ti pozyjesz bardzo dlugo!"
