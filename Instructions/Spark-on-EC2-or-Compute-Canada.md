# Walkthrough

Ian Milligan (University of Waterloo)

This is a walkthrough for installing Warcbase and Spark on a Ubuntu_14.04_Trusty x86_64 (QCOW2) image provided for Compute Canada. Presumably Amazon EC2 would provide a similar sort of experience. For more information on Warcbase, [check out the repository here](https://github.com/lintool/warcbase).

It is a bit bare boned as it assumes some knowledge of a command line environment.

### Step One: SSH to the server 
- For me on a Compute Canada instance, it's `ssh -i macpro.key ubuntu@IPADDRESS`.

### Step Two: Install dependencies
- `sudo apt-get update`
- `sudo apt-get install htop`
- `sudo apt-get install git`
- `sudo apt-get install maven`
- `sudo apt-get install scala`
- `export JAVA_HOME=/usr/lib/jvm/java-7-openjdk-amd64`
- `sudo apt-get install openjdk-7-jdk`

### Step Three: Set up the server properly
- type `echo $HOSTNAME`
- try `ping $HOSTNAME`: if it responds with something like `ping: unknown host milligan-wahr-05` you need to add an entry to your `/etc/hosts` file
- `sudo vim /etc/hosts`
- replace the `localhost` entry with your hostname - in my case, the first line now reads: `127.0.0.1 milligan-wahr-05`
- now try to `ping $HOSTNAME`: if you begin to see packet transmission/receipt information, you're golden.

### Step Four: Install Spark
- download spark 1.5.1 from [here](http://spark.apache.org/downloads.html). I used [this version for direct download](http://d3kbcqa49mib13.cloudfront.net/spark-1.5.1-bin-hadoop2.6.tgz).
	- for the lazier among us: `wget http://d3kbcqa49mib13.cloudfront.net/spark-1.5.1-bin-hadoop2.6.tgz`
	- `tar -xvf spark-1.5.1-bin-hadoop2.6.tgz`
	- remove the tar file: `rm spark-1.5.1-bin-hadoop2.6.tgz`

### Step Five: Install Warcbase
- bring yourself back to your home directory: `cd --`
- download warcbase: `git clone https://github.com/lintool/warcbase.git`
- change to the warcbase directory: `cd warcbase`
- build warcbase: `mvn clean package appassembler:assemble -DskipTests`

### Step Six: Test that Warcbase and Spark are working
- verify that the shell works by navigating to your spark-shell directory and running: `./bin/spark-shell`
- if you don't get a bunch of errors, try: `./bin/spark-shell --jars /home/ubuntu/warcbase/target/warcbase-0.1.0-SNAPSHOT-fatjar.jar` to initalize warcbase
- Try this following script. In order to paste code, type `paste` and then Ctrl+D when you finish it up.

```
val r = RecordLoader.loadArc("/home/ubuntu/warcbase/src/test/resources/arc/example.arc.gz", sc)
  .keepValidPages()
  .map(r => ExtractTopLevelDomain(r.getUrl))
  .countItems()
  .take(10)
```
 
If you receive the following output:

```
r: Array[(String, Int)] = Array((www.archive.org,132), (deadlists.com,2), (www.hideout.com.br,1))
```

Then you're working.

### Step Seven: Getting the Spark Notebook working
- download it with this command: `wget https://s3.eu-central-1.amazonaws.com/spark-notebook/tgz/spark-notebook-master-scala-2.10.4-spark-1.5.1-hadoop-2.6.0-cdh5.4.2.tgz`
- unzip it: `tar -xvf spark-notebook-master-scala-2.10.4-spark-1.5.1-hadoop-2.6.0-cdh5.4.2.tgz`
- test that it works: `./bin/spark-notebook`

The catch is that you'll want to view it on a browser, but you're working on a server. 

### Step Eight: Deployment
While it is easy to deploy, at least for quick testing purposes, with `sudo ./bin/spark-notebook -Dhttp.port=80`, this will leave your Spark Notebook wide open to the world. As you've got read/write privileges, unless you really don't care about your machine or your data, this isn't the best way.

Instead, open an SSH tunnel to your instance. You'll need to reconnect using `ssh`. The following command should establish a tunnel from the remote localhost:9000 to your local localhost:9000.

`ssh -i macpro.key ubuntu@MYIPADDRESS -L 9000:127.0.0.1:9000`

Once in, deploy your Spark Notebook by running

`sudo ./bin/spark-notebook -Dhttp.port=9000` from your spark-notebook directory (in my case, that is `~/spark-notebook-0.6.2-SNAPSHOT-scala-2.10.4-spark-1.5.1-hadoop-2.6.0-cdh5.4.2`).

On your local browser, point it to `localhost:9000`. You should see your spark-notebook!

![the spark notebook in action](https://raw.githubusercontent.com/ianmilligan1/WAHR/master/images/Spark-Notebook-Cluster.png)

### Step Nine: Tweaking
You might find that your jobs are taking too long. This might because you don't have enough executors set. 

Find how many CPU cores you have free by running `htop`. On a lightweight cloud machine, you might see:

![four cores in action](https://raw.githubusercontent.com/ianmilligan1/WAHR/master/images/four-cores.png)

This shows four cores in action. So when you run your `spark-shell` as in Step Six above, you might want to pass `--num-executors 4`. Tweak and refine as needed.

### Step Ten: Have Fun
You've now got warcbase running in the cloud. What more could a person want?