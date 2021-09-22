#!/bin/bash
nohup python3 download_copy_test_empresas.py &
nohup python3 download_copy_test_empresas2.py &
nohup python3 download_copy_test_estabele.py &
nohup python3 download_copy_test_estabele2.py &
nohup python3 download_copy_test_socio.py &
nohup python3 download_copy_test_socio2.py &
nohup python3 download_copy_test_outros.py &
wait