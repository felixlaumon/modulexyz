# modulexyz

Opinionated python module template

## Setup

    license-generator install mit -y $(date +'%Y') -n "Your Name" -e md
    npm -g install license-generator
    rm -rf .git

    ack -l 'modulexyz' | xargs perl -pi -E 's/modulexyz/new_module_name/g'
    mv modulexyz/ new_module_name/

    sphnix-quickstart

## References

- https://github.com/kennethreitz/samplemod
- http://docs.python-guide.org/en/latest/writing/structure/
