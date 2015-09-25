#!/usr/bin/env python
# -*- coding:utf-8 -*- 


##############################################################################
## license :
##============================================================================
##
## File :        EigerDectris.py
## 
## Project :     Eiger Detector
##
## This file is part of Tango device class.
## 
## Tango is free software: you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation, either version 3 of the License, or
## (at your option) any later version.
## 
## Tango is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.
## 
## You should have received a copy of the GNU General Public License
## along with Tango.  If not, see <http://www.gnu.org/licenses/>.
## 
##
## $Author :      tnunez$
##
## $Revision :    $
##
## $Date :        $
##
## $HeadUrl :     $
##============================================================================
##            This file is generated by POGO
##    (Program Obviously used to Generate tango Object)
##
##        (c) - Software Engineering Group - ESRF
##############################################################################

"""Class for controlling the Eiger detector from Dectris"""

__all__ = ["EigerDectris", "EigerDectrisClass", "main"]

__docformat__ = 'restructuredtext'

import PyTango
import sys
# Add additional import
#----- PROTECTED REGION ID(EigerDectris.additionnal_import) ENABLED START -----#

from dectris_eiger.eiger import EigerDetector
import json
from threading import Thread

#----- PROTECTED REGION END -----#	//	EigerDectris.additionnal_import

## Device States Description
## ON : 
## FAULT : 
## MOVING : 

class EigerDectris (PyTango.Device_4Impl):

    #--------- Add you global variables here --------------------------
    #----- PROTECTED REGION ID(EigerDectris.global_variables) ENABLED START -----#
    
    #----- PROTECTED REGION END -----#	//	EigerDectris.global_variables

    def __init__(self,cl, name):
        PyTango.Device_4Impl.__init__(self,cl,name)
        self.debug_stream("In __init__()")
        EigerDectris.init_device(self)
        #----- PROTECTED REGION ID(EigerDectris.__init__) ENABLED START -----#
        

        #----- PROTECTED REGION END -----#	//	EigerDectris.__init__
        
    def delete_device(self):
        self.debug_stream("In delete_device()")
        #----- PROTECTED REGION ID(EigerDectris.delete_device) ENABLED START -----#
        
        #----- PROTECTED REGION END -----#	//	EigerDectris.delete_device

    def init_device(self):
        self.debug_stream("In init_device()")
        self.get_device_properties(self.get_device_class())
        self.attr_NbImages_read = 0
        self.attr_Temperature_read = 0.0
        self.attr_Humidity_read = 0.0
        self.attr_CountTime_read = 0.0
        self.attr_FrameTime_read = 0.0
        self.attr_Energy_read = 0.0
        self.attr_Wavelength_read = 0.0
        self.attr_EnergyThreshold_read = 0.0
        self.attr_FlatfieldEnabled_read = 0
        self.attr_AutoSummationEnabled_read = 0
        self.attr_TriggerMode_read = ''
        self.attr_RateCorrectionEnabled_read = 0
        self.attr_BitDepth_read = 0.0
        self.attr_ReadoutTime_read = 0.0
        self.attr_Description_read = ''
        self.attr_ImagesPerFile_read = 0
        self.attr_FilenamePattern_read = ''
        self.attr_CompressionEnabled_read = 0
        self.attr_FileDir_read = ''
        self.attr_FilesToSave_read = ''
        self.attr_FilesInBuffer_read = ['']
        #----- PROTECTED REGION ID(EigerDectris.init_device) ENABLED START -----#
        
        print "Detector being initialized. This can take about 20 s ..."

        nums = self.APIVersion.split(".")

        if int(nums[1]) > 2:
            self.PortNb = -1

        self.det = EigerDetector(self.Host, self.PortNb,self.APIVersion)

        self.flag_arm = 0

        # initialize the detector
        self.det.initialize()
        print "Detector initialized"
        
        #----- PROTECTED REGION END -----#	//	EigerDectris.init_device

    def always_executed_hook(self):
        self.debug_stream("In always_excuted_hook()")
        #----- PROTECTED REGION ID(EigerDectris.always_executed_hook) ENABLED START -----#
        
        #----- PROTECTED REGION END -----#	//	EigerDectris.always_executed_hook

    #-----------------------------------------------------------------------------
    #    EigerDectris read/write attribute methods
    #-----------------------------------------------------------------------------
    
    def read_NbImages(self, attr):
        self.debug_stream("In read_NbImages()")
        #----- PROTECTED REGION ID(EigerDectris.NbImages_read) ENABLED START -----#
        
        if self.flag_arm == 0 and self.get_state() != PyTango.DevState.MOVING:
            self.attr_NbImages_read = self.det.nimages

        attr.set_value(self.attr_NbImages_read)
        
        #----- PROTECTED REGION END -----#	//	EigerDectris.NbImages_read
        
    def write_NbImages(self, attr):
        self.debug_stream("In write_NbImages()")
        data=attr.get_write_value()
        #----- PROTECTED REGION ID(EigerDectris.NbImages_write) ENABLED START -----#
        
        self.det.nimages = data

        #----- PROTECTED REGION END -----#	//	EigerDectris.NbImages_write
        
    def read_Temperature(self, attr):
        self.debug_stream("In read_Temperature()")
        #----- PROTECTED REGION ID(EigerDectris.Temperature_read) ENABLED START -----#

        if self.flag_arm == 0 and self.get_state() != PyTango.DevState.MOVING:
            self.attr_Temperature_read = self.det.temperature
        attr.set_value(self.attr_Temperature_read)
        
        #----- PROTECTED REGION END -----#	//	EigerDectris.Temperature_read
        
    def read_Humidity(self, attr):
        self.debug_stream("In read_Humidity()")
        #----- PROTECTED REGION ID(EigerDectris.Humidity_read) ENABLED START -----#

        if self.flag_arm == 0 and self.get_state() != PyTango.DevState.MOVING:
            self.attr_Humidity_read = self.det.humidity
        attr.set_value(self.attr_Humidity_read)
        
        #----- PROTECTED REGION END -----#	//	EigerDectris.Humidity_read
        
    def read_CountTime(self, attr):
        self.debug_stream("In read_CountTime()")
        #----- PROTECTED REGION ID(EigerDectris.CountTime_read) ENABLED START -----#

        if self.flag_arm == 0 and self.get_state() != PyTango.DevState.MOVING:
            self.attr_CountTime_read = self.det.count_time
        attr.set_value(self.attr_CountTime_read)
        
        #----- PROTECTED REGION END -----#	//	EigerDectris.CountTime_read
        
    def write_CountTime(self, attr):
        self.debug_stream("In write_CountTime()")
        data=attr.get_write_value()
        #----- PROTECTED REGION ID(EigerDectris.CountTime_write) ENABLED START -----#

        self.det.count_time = data

        #----- PROTECTED REGION END -----#	//	EigerDectris.CountTime_write
        
    def read_FrameTime(self, attr):
        self.debug_stream("In read_FrameTime()")
        #----- PROTECTED REGION ID(EigerDectris.FrameTime_read) ENABLED START -----#

        if self.flag_arm == 0 and self.get_state() != PyTango.DevState.MOVING:
            self.attr_FrameTime_read = self.det.frame_time
        attr.set_value(self.attr_FrameTime_read)
        
        #----- PROTECTED REGION END -----#	//	EigerDectris.FrameTime_read
        
    def write_FrameTime(self, attr):
        self.debug_stream("In write_FrameTime()")
        data=attr.get_write_value()
        #----- PROTECTED REGION ID(EigerDectris.FrameTime_write) ENABLED START -----#
        
        self.det.frame_time = data
        
        #----- PROTECTED REGION END -----#	//	EigerDectris.FrameTime_write
        
    def read_Energy(self, attr):
        self.debug_stream("In read_Energy()")
        #----- PROTECTED REGION ID(EigerDectris.Energy_read) ENABLED START -----#

        if self.flag_arm == 0 and self.get_state() != PyTango.DevState.MOVING:
            self.attr_Energy_read = self.det.energy
        attr.set_value(self.attr_Energy_read)
        
        #----- PROTECTED REGION END -----#	//	EigerDectris.Energy_read
        
    def write_Energy(self, attr):
        self.debug_stream("In write_Energy()")
        data=attr.get_write_value()
        #----- PROTECTED REGION ID(EigerDectris.Energy_write) ENABLED START -----#
        
        self.det.energy = data
        
        #----- PROTECTED REGION END -----#	//	EigerDectris.Energy_write
        
    def read_Wavelength(self, attr):
        self.debug_stream("In read_Wavelength()")
        #----- PROTECTED REGION ID(EigerDectris.Wavelength_read) ENABLED START -----#
        
        if self.flag_arm == 0 and self.get_state() != PyTango.DevState.MOVING:
            self.attr_Wavelength_read = self.det.wavelength
        attr.set_value(self.attr_Wavelength_read)
        
        #----- PROTECTED REGION END -----#	//	EigerDectris.Wavelength_read
        
    def write_Wavelength(self, attr):
        self.debug_stream("In write_Wavelength()")
        data=attr.get_write_value()
        #----- PROTECTED REGION ID(EigerDectris.Wavelength_write) ENABLED START -----#
        
        self.det.wavelength = data

        #----- PROTECTED REGION END -----#	//	EigerDectris.Wavelength_write
        
    def read_EnergyThreshold(self, attr):
        self.debug_stream("In read_EnergyThreshold()")
        #----- PROTECTED REGION ID(EigerDectris.EnergyThreshold_read) ENABLED START -----#

        if self.flag_arm == 0 and self.get_state() != PyTango.DevState.MOVING:
            self.attr_EnergyThreshold_read = self.det.threshold
        attr.set_value(self.attr_EnergyThreshold_read)
        
        #----- PROTECTED REGION END -----#	//	EigerDectris.EnergyThreshold_read
        
    def write_EnergyThreshold(self, attr):
        self.debug_stream("In write_EnergyThreshold()")
        data=attr.get_write_value()
        #----- PROTECTED REGION ID(EigerDectris.EnergyThreshold_write) ENABLED START -----#
        
        self.det.threshold = data

        #----- PROTECTED REGION END -----#	//	EigerDectris.EnergyThreshold_write
        
    def read_FlatfieldEnabled(self, attr):
        self.debug_stream("In read_FlatfieldEnabled()")
        #----- PROTECTED REGION ID(EigerDectris.FlatfieldEnabled_read) ENABLED START -----#
        
        if self.flag_arm == 0 and self.get_state() != PyTango.DevState.MOVING:
            self.attr_FlatfieldEnabled_read = 0
            if self.det.flatfield_enabled == True:
                self.attr_FlatfieldEnabled_read = 1
            
        attr.set_value(self.attr_FlatfieldEnabled_read)
        
        #----- PROTECTED REGION END -----#	//	EigerDectris.FlatfieldEnabled_read
        
    def write_FlatfieldEnabled(self, attr):
        self.debug_stream("In write_FlatfieldEnabled()")
        data=attr.get_write_value()
        #----- PROTECTED REGION ID(EigerDectris.FlatfieldEnabled_write) ENABLED START -----#
        
        if data == 0:
            self.det.flatfield_enabled = False
        else:
            self.det.flatfield_enabled = True
        #----- PROTECTED REGION END -----#	//	EigerDectris.FlatfieldEnabled_write
        
    def read_AutoSummationEnabled(self, attr):
        self.debug_stream("In read_AutoSummationEnabled()")
        #----- PROTECTED REGION ID(EigerDectris.AutoSummationEnabled_read) ENABLED START -----#
        
        if self.flag_arm == 0 and self.get_state() != PyTango.DevState.MOVING:
            self.attr_AutoSummationEnabled_read = 0
            if self.det.auto_summation_enabled == True:
                self.attr_AutoSummationEnabled_read = 1
            
        attr.set_value(self.attr_AutoSummationEnabled_read)
        
        #----- PROTECTED REGION END -----#	//	EigerDectris.AutoSummationEnabled_read
        
    def write_AutoSummationEnabled(self, attr):
        self.debug_stream("In write_AutoSummationEnabled()")
        data=attr.get_write_value()
        #----- PROTECTED REGION ID(EigerDectris.AutoSummationEnabled_write) ENABLED START -----#
        
        if data == 0:
            self.det.auto_summation_enabled = False
        else:
            self.det.auto_summation_enabled = True

        #----- PROTECTED REGION END -----#	//	EigerDectris.AutoSummationEnabled_write
        
    def read_TriggerMode(self, attr):
        self.debug_stream("In read_TriggerMode()")
        #----- PROTECTED REGION ID(EigerDectris.TriggerMode_read) ENABLED START -----#

        if self.flag_arm == 0 and self.get_state() != PyTango.DevState.MOVING:
            self.attr_TriggerMode_read = self.det.trigger_mode
        attr.set_value(self.attr_TriggerMode_read)
        
        #----- PROTECTED REGION END -----#	//	EigerDectris.TriggerMode_read
        
    def write_TriggerMode(self, attr):
        self.debug_stream("In write_TriggerMode()")
        data=attr.get_write_value()
        #----- PROTECTED REGION ID(EigerDectris.TriggerMode_write) ENABLED START -----#
        
        self.det.trigger_mode = data

        #----- PROTECTED REGION END -----#	//	EigerDectris.TriggerMode_write
        
    def read_RateCorrectionEnabled(self, attr):
        self.debug_stream("In read_RateCorrectionEnabled()")
        #----- PROTECTED REGION ID(EigerDectris.RateCorrectionEnabled_read) ENABLED START -----#
        
        if self.flag_arm == 0 and self.get_state() != PyTango.DevState.MOVING:
            self.attr_RateCorrectionEnabled_read = 0
            if self.det.rate_correction_enabled == True:
                self.attr_RateCorrectionEnabled_read = 1
        attr.set_value(self.attr_RateCorrectionEnabled_read)
        
        #----- PROTECTED REGION END -----#	//	EigerDectris.RateCorrectionEnabled_read
        
    def write_RateCorrectionEnabled(self, attr):
        self.debug_stream("In write_RateCorrectionEnabled()")
        data=attr.get_write_value()
        #----- PROTECTED REGION ID(EigerDectris.RateCorrectionEnabled_write) ENABLED START -----#
        
        if data == 0:
            self.det.rate_correction_enabled = False
        else:
            self.det.rate_correction_enabled = True

        #----- PROTECTED REGION END -----#	//	EigerDectris.RateCorrectionEnabled_write
        
    def read_BitDepth(self, attr):
        self.debug_stream("In read_BitDepth()")
        #----- PROTECTED REGION ID(EigerDectris.BitDepth_read) ENABLED START -----#

        if self.flag_arm == 0 and self.get_state() != PyTango.DevState.MOVING:
            self.attr_BitDepth_read = self.det.bit_depth
        attr.set_value(self.attr_BitDepth_read)
        
        #----- PROTECTED REGION END -----#	//	EigerDectris.BitDepth_read
        
    def read_ReadoutTime(self, attr):
        self.debug_stream("In read_ReadoutTime()")
        #----- PROTECTED REGION ID(EigerDectris.ReadoutTime_read) ENABLED START -----#
        
        if self.flag_arm == 0 and self.get_state() != PyTango.DevState.MOVING:
            self.attr_ReadoutTime_read = self.det.readout_time
        attr.set_value(self.attr_ReadoutTime_read)
        
        #----- PROTECTED REGION END -----#	//	EigerDectris.ReadoutTime_read
        
    def read_Description(self, attr):
        self.debug_stream("In read_Description()")
        #----- PROTECTED REGION ID(EigerDectris.Description_read) ENABLED START -----#

        if self.flag_arm == 0 and self.get_state() != PyTango.DevState.MOVING:
            self.attr_Description_read = self.det.description
        attr.set_value(self.attr_Description_read)
        
        #----- PROTECTED REGION END -----#	//	EigerDectris.Description_read
        
    def read_ImagesPerFile(self, attr):
        self.debug_stream("In read_ImagesPerFile()")
        #----- PROTECTED REGION ID(EigerDectris.ImagesPerFile_read) ENABLED START -----#

        if self.flag_arm == 0 and self.get_state() != PyTango.DevState.MOVING:
            self.attr_ImagesPerFile_read = self.det.filewriter.images_per_file
        attr.set_value(self.attr_ImagesPerFile_read)
        
        #----- PROTECTED REGION END -----#	//	EigerDectris.ImagesPerFile_read
        
    def write_ImagesPerFile(self, attr):
        self.debug_stream("In write_ImagesPerFile()")
        data=attr.get_write_value()
        #----- PROTECTED REGION ID(EigerDectris.ImagesPerFile_write) ENABLED START -----#
        
        self.det.filewriter.images_per_file = data

        #----- PROTECTED REGION END -----#	//	EigerDectris.ImagesPerFile_write
        
    def read_FilenamePattern(self, attr):
        self.debug_stream("In read_FilenamePattern()")
        #----- PROTECTED REGION ID(EigerDectris.FilenamePattern_read) ENABLED START -----#

        if self.flag_arm == 0 and self.get_state() != PyTango.DevState.MOVING:
            self.attr_FilenamePattern_read = self.det.filewriter.filename_pattern
        attr.set_value(self.attr_FilenamePattern_read)
        
        #----- PROTECTED REGION END -----#	//	EigerDectris.FilenamePattern_read
        
    def write_FilenamePattern(self, attr):
        self.debug_stream("In write_FilenamePattern()")
        data=attr.get_write_value()
        #----- PROTECTED REGION ID(EigerDectris.FilenamePattern_write) ENABLED START -----#
        
        self.det.filewriter.filename_pattern = data

        #----- PROTECTED REGION END -----#	//	EigerDectris.FilenamePattern_write
        
    def read_CompressionEnabled(self, attr):
        self.debug_stream("In read_CompressionEnabled()")
        #----- PROTECTED REGION ID(EigerDectris.CompressionEnabled_read) ENABLED START -----#
        
        if self.flag_arm == 0 and self.get_state() != PyTango.DevState.MOVING:
            self.attr_CompressionEnabled_read = 0
            if self.det.filewriter.compression_enabled == True:
                self.attr_CompressionEnabled_read = 1
            
        attr.set_value(self.attr_CompressionEnabled_read)
        
        #----- PROTECTED REGION END -----#	//	EigerDectris.CompressionEnabled_read
        
    def write_CompressionEnabled(self, attr):
        self.debug_stream("In write_CompressionEnabled()")
        data=attr.get_write_value()
        #----- PROTECTED REGION ID(EigerDectris.CompressionEnabled_write) ENABLED START -----#
        
        if data == 0:
            self.det.filewriter.compression_enabled = False
        else:
            self.det.filewriter.compression_enabled = True

        #----- PROTECTED REGION END -----#	//	EigerDectris.CompressionEnabled_write
        
    def read_FileDir(self, attr):
        self.debug_stream("In read_FileDir()")
        #----- PROTECTED REGION ID(EigerDectris.FileDir_read) ENABLED START -----#
        attr.set_value(self.attr_FileDir_read)
        
        #----- PROTECTED REGION END -----#	//	EigerDectris.FileDir_read
        
    def write_FileDir(self, attr):
        self.debug_stream("In write_FileDir()")
        data=attr.get_write_value()
        #----- PROTECTED REGION ID(EigerDectris.FileDir_write) ENABLED START -----#
        
        self.attr_FileDir_read = data

        #----- PROTECTED REGION END -----#	//	EigerDectris.FileDir_write
        
    def read_FilesToSave(self, attr):
        self.debug_stream("In read_FilesToSave()")
        #----- PROTECTED REGION ID(EigerDectris.FilesToSave_read) ENABLED START -----#
        attr.set_value(self.attr_FilesToSave_read)
        
        #----- PROTECTED REGION END -----#	//	EigerDectris.FilesToSave_read
        
    def write_FilesToSave(self, attr):
        self.debug_stream("In write_FilesToSave()")
        data=attr.get_write_value()
        #----- PROTECTED REGION ID(EigerDectris.FilesToSave_write) ENABLED START -----#
        
        self.attr_FilesToSave_read = data
        
        #----- PROTECTED REGION END -----#	//	EigerDectris.FilesToSave_write
        
    def read_FilesInBuffer(self, attr):
        self.debug_stream("In read_FilesInBuffer()")
        #----- PROTECTED REGION ID(EigerDectris.FilesInBuffer_read) ENABLED START -----#
        
        nb_files = 0
        for file_name in self.det.buffer.files:
            self.attr_FilesInBuffer_read.append(str(file_name))
            nb_files = nb_files + 1
        
        attr.set_value(self.attr_FilesInBuffer_read, nb_files)
        
        #----- PROTECTED REGION END -----#	//	EigerDectris.FilesInBuffer_read
        
    
    
        #----- PROTECTED REGION ID(EigerDectris.initialize_dynamic_attributes) ENABLED START -----#
        
        #----- PROTECTED REGION END -----#	//	EigerDectris.initialize_dynamic_attributes
            
    def read_attr_hardware(self, data):
        self.debug_stream("In read_attr_hardware()")
        #----- PROTECTED REGION ID(EigerDectris.read_attr_hardware) ENABLED START -----#
        
        #----- PROTECTED REGION END -----#	//	EigerDectris.read_attr_hardware


    #-----------------------------------------------------------------------------
    #    EigerDectris command methods
    #-----------------------------------------------------------------------------
    
    def dev_state(self):
        """ This command gets the device state (stored in its device_state data member) and returns it to the caller.
        
        :param : none
        :type: PyTango.DevVoid
        :return: Device state
        :rtype: PyTango.CmdArgType.DevState """
        self.debug_stream("In dev_state()")
        argout = PyTango.DevState.UNKNOWN
        #----- PROTECTED REGION ID(EigerDectris.State) ENABLED START -----#
        
        rstate = self.det.get_state()

        if self.flag_arm:
            if rstate == "configure" or rstate == "ready":
                self.flag_arm = 0

        if rstate == "error":
            self.set_state(PyTango.DevState.FAULT) 
        elif (rstate != "idle" and rstate != "ready") or self.flag_arm:
            self.set_state(PyTango.DevState.MOVING)
        else:
            self.set_state(PyTango.DevState.ON) 

        self.set_status(str(rstate))

        argout = self.get_state()
        
        #----- PROTECTED REGION END -----#	//	EigerDectris.State
        if argout != PyTango.DevState.ALARM:
            PyTango.Device_4Impl.dev_state(self)
        return self.get_state()
        
    def dev_status(self):
        """ This command gets the device status (stored in its device_status data member) and returns it to the caller.
        
        :param : none
        :type: PyTango.DevVoid
        :return: Device status
        :rtype: PyTango.ConstDevString """
        self.debug_stream("In dev_status()")
        argout = ''
        #----- PROTECTED REGION ID(EigerDectris.Status) ENABLED START -----#
               
        rstate = self.det.get_state()

        self.argout = str(rstate)

        #----- PROTECTED REGION END -----#	//	EigerDectris.Status
        self.set_status(self.argout)
        self.__status = PyTango.Device_4Impl.dev_status(self)
        return self.__status
        
    def Arm(self, argin):
        """ Arm/Disarm the detector.
        
        :param argin: 0-> Disarm, 1 -> Arm
        :type: PyTango.DevLong
        :return: 
        :rtype: PyTango.DevVoid """
        self.debug_stream("In Arm()")
        #----- PROTECTED REGION ID(EigerDectris.Arm) ENABLED START -----#
        
        rstate = self.det.get_state()

        if argin == 1:
            if rstate != "ready":
                try:
                    self.flag_arm = 1
                    self.det.arm(timeout=0.1)
                except:
                    pass
        else:
            if rstate != "idle":
                self.flag_arm = 0
                self.det.disarm()
        
        #----- PROTECTED REGION END -----#	//	EigerDectris.Arm
        
    def Trigger(self):
        """ Trigger the detector.
        
        :param : 
        :type: PyTango.DevVoid
        :return: 
        :rtype: PyTango.DevVoid """
        self.debug_stream("In Trigger()")
        #----- PROTECTED REGION ID(EigerDectris.Trigger) ENABLED START -----#
        
        rstate = self.det.get_state()

        if rstate != "ready":
            raise Exception("Detector in %s state, not 'ready',  try the arm command first" % str(rstate))

            self.det.trigger()

        #----- PROTECTED REGION END -----#	//	EigerDectris.Trigger
        
    def Abort(self):
        """ Abort all operations and reset the detector system.
        
        :param : 
        :type: PyTango.DevVoid
        :return: 
        :rtype: PyTango.DevVoid """
        self.debug_stream("In Abort()")
        #----- PROTECTED REGION ID(EigerDectris.Abort) ENABLED START -----#

        self.det.abort()

        #----- PROTECTED REGION END -----#	//	EigerDectris.Abort
        
    def Cancel(self):
        """ Stop data acquisition after the current image.
        
        :param : 
        :type: PyTango.DevVoid
        :return: 
        :rtype: PyTango.DevVoid """
        self.debug_stream("In Cancel()")
        #----- PROTECTED REGION ID(EigerDectris.Cancel) ENABLED START -----#

        self.det.cancel()

        #----- PROTECTED REGION END -----#	//	EigerDectris.Cancel
        
    def SaveFiles(self):
        """ Save the files matching FilesToSave to FileDir
        
        :param : 
        :type: PyTango.DevVoid
        :return: 
        :rtype: PyTango.DevVoid """
        self.debug_stream("In SaveFiles()")
        #----- PROTECTED REGION ID(EigerDectris.SaveFiles) ENABLED START -----#
        
        file_pattern = self.attr_FilesToSave_read + "*"

        
        th = CommonThread(0,self.det, file_pattern,self.attr_FileDir_read)
        th.start()
        
        #----- PROTECTED REGION END -----#	//	EigerDectris.SaveFiles
        
    def ClearBuffer(self):
        """ Delete all files from buffer
        
        :param : 
        :type: PyTango.DevVoid
        :return: 
        :rtype: PyTango.DevVoid """
        self.debug_stream("In ClearBuffer()")
        #----- PROTECTED REGION ID(EigerDectris.ClearBuffer) ENABLED START -----#
        
        self.det.clear_buffer()

        #----- PROTECTED REGION END -----#	//	EigerDectris.ClearBuffer
        
    def DeleteFileFromBuffer(self, argin):
        """ Delete the file give the argument name from the buffer
        
        :param argin: Name of the file to delete
        :type: PyTango.DevString
        :return: 
        :rtype: PyTango.DevVoid """
        self.debug_stream("In DeleteFileFromBuffer()")
        #----- PROTECTED REGION ID(EigerDectris.DeleteFileFromBuffer) ENABLED START -----#

        self.det.buffer.delete_file(argin)

        #----- PROTECTED REGION END -----#	//	EigerDectris.DeleteFileFromBuffer
        

    #----- PROTECTED REGION ID(EigerDectris.programmer_methods) ENABLED START -----#
    
    #----- PROTECTED REGION END -----#	//	EigerDectris.programmer_methods

class EigerDectrisClass(PyTango.DeviceClass):
    #--------- Add you global class variables here --------------------------
    #----- PROTECTED REGION ID(EigerDectris.global_class_variables) ENABLED START -----#
    
    #----- PROTECTED REGION END -----#	//	EigerDectris.global_class_variables

    def dyn_attr(self, dev_list):
        """Invoked to create dynamic attributes for the given devices.
        Default implementation calls
        :meth:`EigerDectris.initialize_dynamic_attributes` for each device
    
        :param dev_list: list of devices
        :type dev_list: :class:`PyTango.DeviceImpl`"""
    
        for dev in dev_list:
            try:
                dev.initialize_dynamic_attributes()
            except:
                import traceback
                dev.warn_stream("Failed to initialize dynamic attributes")
                dev.debug_stream("Details: " + traceback.format_exc())
        #----- PROTECTED REGION ID(EigerDectris.dyn_attr) ENABLED START -----#
        
        #----- PROTECTED REGION END -----#	//	EigerDectris.dyn_attr

    #    Class Properties
    class_property_list = {
        }


    #    Device Properties
    device_property_list = {
        'Host':
            [PyTango.DevString,
            "Host name",
            [] ],
        'PortNb':
            [PyTango.DevLong,
            "Port number",
            [80]],
        'APIVersion':
            [PyTango.DevString,
            "API Version, ex. 1.0.0",
            ["1.0.0"] ],
        }


    #    Command definitions
    cmd_list = {
        'Arm':
            [[PyTango.DevLong, "0-> Disarm, 1 -> Arm"],
            [PyTango.DevVoid, "none"]],
        'Trigger':
            [[PyTango.DevVoid, "none"],
            [PyTango.DevVoid, "none"]],
        'Abort':
            [[PyTango.DevVoid, "none"],
            [PyTango.DevVoid, "none"]],
        'Cancel':
            [[PyTango.DevVoid, "none"],
            [PyTango.DevVoid, "none"]],
        'SaveFiles':
            [[PyTango.DevVoid, "none"],
            [PyTango.DevVoid, "none"]],
        'ClearBuffer':
            [[PyTango.DevVoid, "none"],
            [PyTango.DevVoid, "none"]],
        'DeleteFileFromBuffer':
            [[PyTango.DevString, "Name of the file to delete"],
            [PyTango.DevVoid, "none"]],
        }


    #    Attribute definitions
    attr_list = {
        'NbImages':
            [[PyTango.DevLong,
            PyTango.SCALAR,
            PyTango.READ_WRITE],
            {
                'description': "Number of images per serie",
            } ],
        'Temperature':
            [[PyTango.DevDouble,
            PyTango.SCALAR,
            PyTango.READ],
            {
                'unit': "Celsius",
                'description': "Board temperature",
            } ],
        'Humidity':
            [[PyTango.DevDouble,
            PyTango.SCALAR,
            PyTango.READ],
            {
                'unit': "%",
                'description': "Returns the relative humidity reading (in percent)",
            } ],
        'CountTime':
            [[PyTango.DevDouble,
            PyTango.SCALAR,
            PyTango.READ_WRITE],
            {
                'unit': "s",
                'description': "Currently set count time per image in seconds",
            } ],
        'FrameTime':
            [[PyTango.DevDouble,
            PyTango.SCALAR,
            PyTango.READ_WRITE],
            {
                'unit': "s",
                'description': "Currently set frame time (count time plus read out time) per image in seconds.",
            } ],
        'Energy':
            [[PyTango.DevDouble,
            PyTango.SCALAR,
            PyTango.READ_WRITE],
            {
                'unit': "eV",
                'description': "Currently set photon energy in electron volts",
            } ],
        'Wavelength':
            [[PyTango.DevDouble,
            PyTango.SCALAR,
            PyTango.READ_WRITE],
            {
                'unit': "A",
                'description': "Currently set photon wavelength in Angstrom.",
            } ],
        'EnergyThreshold':
            [[PyTango.DevDouble,
            PyTango.SCALAR,
            PyTango.READ_WRITE],
            {
                'unit': "eV",
                'description': "Currently set energy threshold in electron volts.",
            } ],
        'FlatfieldEnabled':
            [[PyTango.DevLong,
            PyTango.SCALAR,
            PyTango.READ_WRITE],
            {
                'description': "1 if the flatfield correction is enabled.",
            } ],
        'AutoSummationEnabled':
            [[PyTango.DevLong,
            PyTango.SCALAR,
            PyTango.READ_WRITE],
            {
                'description': "1 if the auto summation feature (to increase the dynamic range) is enabled.",
            } ],
        'TriggerMode':
            [[PyTango.DevString,
            PyTango.SCALAR,
            PyTango.READ_WRITE],
            {
                'description': "Current trigger mode. Following trigger modes are supported:\nexpo, extt, extm, exte, exts, ints",
            } ],
        'RateCorrectionEnabled':
            [[PyTango.DevLong,
            PyTango.SCALAR,
            PyTango.READ_WRITE],
            {
                'description': "1 if the rate correction is enabled.",
            } ],
        'BitDepth':
            [[PyTango.DevDouble,
            PyTango.SCALAR,
            PyTango.READ],
            {
                'description': " Detector  bit depth, i.e. the dynamic range.",
            } ],
        'ReadoutTime':
            [[PyTango.DevDouble,
            PyTango.SCALAR,
            PyTango.READ],
            {
                'unit': "s",
                'description': "detector's readout time per image",
            } ],
        'Description':
            [[PyTango.DevString,
            PyTango.SCALAR,
            PyTango.READ],
            {
                'description': "Detector description, i.e. the model.",
            } ],
        'ImagesPerFile':
            [[PyTango.DevLong,
            PyTango.SCALAR,
            PyTango.READ_WRITE],
            {
                'description': "Number of images stored in a single data file.",
            } ],
        'FilenamePattern':
            [[PyTango.DevString,
            PyTango.SCALAR,
            PyTango.READ_WRITE],
            {
                'description': "The file naming pattern. The string ``$id`` is replaced by the series id.",
            } ],
        'CompressionEnabled':
            [[PyTango.DevLong,
            PyTango.SCALAR,
            PyTango.READ_WRITE],
            {
                'description': "1 if the LZ4 data compression is enabled.",
            } ],
        'FileDir':
            [[PyTango.DevString,
            PyTango.SCALAR,
            PyTango.READ_WRITE],
            {
                'description': "Directory for saving the files",
                'Memorized':"true"
            } ],
        'FilesToSave':
            [[PyTango.DevString,
            PyTango.SCALAR,
            PyTango.READ_WRITE],
            {
                'description': "Pattern of the files to save in FileDir",
                'Memorized':"true"
            } ],
        'FilesInBuffer':
            [[PyTango.DevString,
            PyTango.SPECTRUM,
            PyTango.READ, 1000],
            {
                'description': "Name of files in detector data directory",
            } ],
        }


def main():
    try:
        py = PyTango.Util(sys.argv)
        py.add_class(EigerDectrisClass,EigerDectris,'EigerDectris')
        #----- PROTECTED REGION ID(EigerDectris.add_classes) ENABLED START -----#
        
        #----- PROTECTED REGION END -----#	//	EigerDectris.add_classes

        U = PyTango.Util.instance()
        U.server_init()
        U.server_run()

    except PyTango.DevFailed,e:
        print '-------> Received a DevFailed exception:',e
    except Exception,e:
        print '-------> An unforeseen exception occured....',e

if __name__ == '__main__':
    main()
