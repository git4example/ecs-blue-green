# A way to test container trafic routing for an ECS Blue/Green Deploy
This is how I was able to validate the operation of of B/G deploys, watching if traffic between the blue and green Target Groups are ever interleaved.

## to run
1. './build.sh' (build the container to be tested)
2. `docker tag appversioncontainer $CONTAINER_REPO`
3. `docker push $CONTAINER_REPO`
4. Create ECS B/G service deploy. If using CodePipeline, feel free to implement the provided taskdef.json and appspec.yml.
5. Update container environment variable 'APP_VER' in new versions of the Task Defition.
6. Deploy new Task Definition revision.
7. `./test-nlb-loop.sh'
