#!/bin/bash
# Run this from the project root directory

pushd handouts
    mkdir -p public
    for f in `ls`; do
        if [ -f $f ]; then  
            EXT=`echo $f | cut -d '.' -f 2 | tr '[:upper:]' '[:lower:]'`
            SHASUM=`sha256sum $f | awk '{print $1}'`
            cp $f public/$SHASUM.$EXT
        fi
    done;

    pushd public
        aws s3 sync . s3://s3.games.jdkaplan.com/handouts --acl=public-read --delete
        #aws s3 sync $1 s3://s3.games.jdkaplan.com/handouts --delete
    popd
popd