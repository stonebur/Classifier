trainloop=true;
while $trainloop; do 
   read -p "Would you like to train a classifier? (y,n): " train
   if [ $train == 'y' ]; then
      echo "Before you begin, be sure to put the images you would like to train the classify in the directory tf_files/catvdog"
      echo "Training classifier with uploaded photos..."
      sh ./train.sh
      trainloop=false;
   elif [ $train == 'n' ]; then 
      trainloop=false;
   else
      echo "Please try again and enter the clearly expressed options"
   fi
done

shouldloop=true;
while $shouldloop; do
   read -p "Would you like analysis done on a picture in the tf_files/test_pic? (y,n): " delconf
if [ $delconf == 'y' ]; then
   read -p "Please enter a filename to be analyzed, remember to include extension: " filename
   python -m scripts.label_image --graph=tf_files/retrained_graph.pb  --image=tf_files/test_pic/$filename
elif [ $delconf == 'n' ]; then
   echo "Goodbye!"
   shouldloop=false;
else
   echo "Enter a valid response y or n";
   shouldloop=true;
fi
done
