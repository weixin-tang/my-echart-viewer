



docker run -itd --name my-echart-viewer --hostname my-echart-viewer -p 8091:8091 --network weixin-network my-echart-viewer 



docker build -t my-echart-viewer .      


http://localhost:8091/echart-render?dataUrl=https://edu.stonybrook.uk/agent/echart-plot.json

 






